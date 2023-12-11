-- Trigger to update SalesTrend when a new sale is inserted
DELIMITER //

CREATE TRIGGER after_insert_sale
    AFTER INSERT
    ON Sales FOR EACH ROW
BEGIN
    -- Your calculations here, for example:
    INSERT INTO SalesTrend (Date, TotalSales, TotalQuantitySold, AverageSaleAmount, TotalCustomers)
    SELECT
        NEW.Date,
        SUM(Amount),
        SUM(Quantity),
        AVG(Amount),
        COUNT(DISTINCT CustomerID)
    FROM Sales
    WHERE Date = NEW.Date
    ON DUPLICATE KEY UPDATE
                         TotalSales = VALUES(TotalSales),
                         TotalQuantitySold = VALUES(TotalQuantitySold),
                         AverageSaleAmount = VALUES(AverageSaleAmount),
                         TotalCustomers = VALUES(TotalCustomers);

    IF NOT EXISTS (
        SELECT 1
        FROM Sales
        WHERE CustomerID = NEW.CustomerID AND Date < NEW.Date
    ) THEN
        -- Increment NewCustomers for the corresponding date
        INSERT INTO SalesTrend (Date, NewCustomers)
        VALUES (NEW.Date, 1)
        ON DUPLICATE KEY UPDATE NewCustomers = NewCustomers + 1;
END IF;

-- Check if the customer is a repeat customer
IF EXISTS (
        SELECT 1
        FROM Sales
        WHERE CustomerID = NEW.CustomerID AND Date < NEW.Date
    ) THEN
        -- Increment RepeatCustomers for the corresponding date
        INSERT INTO SalesTrend (Date, RepeatCustomers)
        VALUES (NEW.Date, 1)
        ON DUPLICATE KEY UPDATE RepeatCustomers = RepeatCustomers + 1;
END IF;

    -- Update ProductPopularity for the corresponding product
INSERT INTO SalesTrend (Date, ProductPopularity)
VALUES (NEW.Date, CONCAT(NEW.ProductID, ':', 1))
    ON DUPLICATE KEY UPDATE
                         ProductPopularity = CONCAT(NEW.ProductID, ':', SUBSTRING_INDEX(ProductPopularity, ':', -1) + 1);

-- Update SalesGrowthPercentage for the corresponding date
INSERT INTO SalesTrend (Date, SalesGrowthPercentage)
VALUES (NEW.Date, (
    SELECT IFNULL(
                   ((TotalSales - LAG(TotalSales) OVER (ORDER BY Date)) / LAG(TotalSales) OVER (ORDER BY Date)) * 100,
                           0)
    FROM SalesTrend
    WHERE Date = NEW.Date
       ))
ON DUPLICATE KEY UPDATE
                     SalesGrowthPercentage = (
                     SELECT IFNULL(
                     ((TotalSales - LAG(TotalSales) OVER (ORDER BY Date)) / LAG(TotalSales) OVER (ORDER BY Date)) * 100,
                     0)
                     FROM SalesTrend
                     WHERE Date = NEW.Date
                     );

-- Update AveragePurchaseFrequency for the corresponding date
INSERT INTO SalesTrend (Date, AveragePurchaseFrequency)
VALUES (NEW.Date, (
    SELECT IFNULL(
                   AVG(DATEDIFF(Date, LAG(Date) OVER (PARTITION BY CustomerID ORDER BY Date))),
                   0
           )
    FROM Sales
    WHERE CustomerID = NEW.CustomerID
))
    ON DUPLICATE KEY UPDATE
                         AveragePurchaseFrequency = (
                         SELECT IFNULL(
                         AVG(DATEDIFF(Date, LAG(Date) OVER (PARTITION BY CustomerID ORDER BY Date))),
                         0
                         )
                         FROM Sales
                         WHERE CustomerID = NEW.CustomerID
                         );

-- Update CustomerRetentionRate for the corresponding date
INSERT INTO SalesTrend (Date, CustomerRetentionRate)
VALUES (NEW.Date, (
    SELECT IFNULL(
                       (COUNT(DISTINCT CASE WHEN Date = NEW.Date THEN CustomerID END) / NULLIF(COUNT(DISTINCT CASE WHEN Date < NEW.Date THEN CustomerID END), 0)) * 100,
                       0
           )
    FROM Sales
))
    ON DUPLICATE KEY UPDATE
                         CustomerRetentionRate = (
                         SELECT IFNULL(
                         (COUNT(DISTINCT CASE WHEN Date = NEW.Date THEN CustomerID END) / NULLIF(COUNT(DISTINCT CASE WHEN Date < NEW.Date THEN CustomerID END), 0)) * 100,
                         0
                         )
                         FROM Sales
                         );

-- Update PromotionEffectiveness for the corresponding date
INSERT INTO SalesTrend (Date, PromotionEffectiveness)
VALUES (NEW.Date, (
    SELECT IFNULL(
                   ((SUM(NEW.Amount) - SUM(NEW.Amount * (1 - IFNULL(Promotions.DiscountPercentage, 0) / 100))) / NULLIF(SUM(NEW.Quantity), 0)),
                   0
           )
    FROM Sales
             LEFT JOIN Promotions ON Sales.PromotionID = Promotions.PromotionID
    WHERE Date = NEW.Date
       ))
ON DUPLICATE KEY UPDATE
                     PromotionEffectiveness = (
                     SELECT IFNULL(
                     ((SUM(NEW.Amount) - SUM(NEW.Amount * (1 - IFNULL(Promotions.DiscountPercentage, 0) / 100))) / NULLIF(SUM(NEW.Quantity), 0)),
                     0
                     )
                     FROM Sales
                     LEFT JOIN Promotions ON Sales.PromotionID = Promotions.PromotionID
                     WHERE Date = NEW.Date
                     );
END //

DELIMITER ;



ALTER TABLE `SalesTrend`
    ADD COLUMN `TotalDiscountAmount` decimal(10,2) DEFAULT NULL,
    ADD COLUMN `TotalPromotionQuantity` int DEFAULT NULL;