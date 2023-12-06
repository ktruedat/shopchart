CREATE TABLE `Customers` (
                             `CustomerID` int NOT NULL,
                             `Name` varchar(255) DEFAULT NULL,
                             `Email` varchar(255) DEFAULT NULL,
                             `Phone` varchar(20) DEFAULT NULL,
                             PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Producers` (
                             `ProducerID` int NOT NULL,
                             `ProducerName` varchar(255) DEFAULT NULL,
                             `ProducerLocation` varchar(255) DEFAULT NULL,
                             PRIMARY KEY (`ProducerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Sales` (
                         `SaleID` int NOT NULL,
                         `ProductID` int DEFAULT NULL,
                         `CustomerID` int DEFAULT NULL,
                         `Quantity` int DEFAULT NULL,
                         `Amount` decimal(10,2) DEFAULT NULL,
                         `PromotionID` int DEFAULT NULL,
                         `Date` date DEFAULT NULL,
                         PRIMARY KEY (`SaleID`),
                         KEY `Date` (`Date`),
                         KEY `ProductID` (`ProductID`),
                         KEY `CustomerID` (`CustomerID`),
                         CONSTRAINT `Sales_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `Products` (`ProductID`),
                         CONSTRAINT `Sales_ibfk_2` FOREIGN KEY (`CustomerID`) REFERENCES `Customers` (`CustomerID`),
                         CONSTRAINT `Sales_ibfk_3` FOREIGN KEY (`PromotionID`) REFERENCES `Promotions` (`PromotionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `Categories` (
                              `CategoryID` int NOT NULL,
                              `CategoryName` varchar(255) DEFAULT NULL,
                              PRIMARY KEY (`CategoryID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Products` (
                            `ProductID` int NOT NULL,
                            `Name` varchar(255) DEFAULT NULL,
                            `CategoryID` int DEFAULT NULL,
                            `Price` decimal(10,2) DEFAULT NULL,
                            `ProducerID` int DEFAULT NULL,
                            PRIMARY KEY (`ProductID`),
                            KEY `ProducerID` (`ProducerID`),
                            CONSTRAINT `Products_ibfk_1` FOREIGN KEY (`ProducerID`) REFERENCES `Producers` (`ProducerID`),
                            CONSTRAINT `Products_ibfk_2` FOREIGN KEY (`CategoryID`) REFERENCES `Categories` (`CategoryID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Promotions` (
                              `PromotionID` int NOT NULL,
                              `PromotionName` varchar(255) DEFAULT NULL,
                              `DiscountPercentage` decimal(5,2) DEFAULT NULL,
                              `StartDate` date DEFAULT NULL,
                              `EndDate` date DEFAULT NULL,
                              PRIMARY KEY (`PromotionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE `SalesTrend` (
                              `SalesTrendID` int NOT NULL AUTO_INCREMENT,
                              `Date` date DEFAULT NULL,
                              `TotalSales` decimal(10,2) DEFAULT NULL,
                              `TotalQuantitySold` int DEFAULT NULL,
                              `AverageSaleAmount` decimal(10,2) DEFAULT NULL,
                              `TotalCustomers` int DEFAULT NULL,
                              `NewCustomers` int DEFAULT NULL,
                              `RepeatCustomers` int DEFAULT NULL,
                              `ProductPopularity` varchar(255) DEFAULT NULL,
                              `CategoryPopularity` varchar(255) DEFAULT NULL,
                              `SalesGrowthPercentage` decimal(5,2) DEFAULT NULL,
                              `AveragePurchaseFrequency` decimal(5,2) DEFAULT NULL,
                              `CustomerRetentionRate` decimal(5,2) DEFAULT NULL,
                              `SeasonalTrends` varchar(255) DEFAULT NULL,
                              `PromotionEffectiveness` varchar(255) DEFAULT NULL,
                              PRIMARY KEY (`SalesTrendID`),
                              UNIQUE KEY `Date` (`Date`),
                              CONSTRAINT `SalesTrend_ibfk_1` FOREIGN KEY (`Date`) REFERENCES `Sales` (`Date`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




DELIMITER //

CREATE TRIGGER after_insert_sale
    AFTER INSERT
    ON Sales FOR EACH ROW
BEGIN
    -- Temporary table to store intermediate results
    CREATE TEMPORARY TABLE temp_results1 (
                                            Date DATE,
                                            TotalSales DECIMAL(10,2),
                                            TotalQuantitySold INT,
                                            AverageSaleAmount DECIMAL(10,2),
                                            TotalCustomers INT,
                                            SaleID INT
    );

    -- Your calculations here, for example:
    INSERT INTO temp_results1 (Date, TotalSales, TotalQuantitySold, AverageSaleAmount, TotalCustomers, SaleID)
    SELECT
        Date,
        SUM(Amount),
        SUM(Quantity),
        AVG(Amount),
        COUNT(DISTINCT CustomerID),
        SaleID
    FROM Sales
    WHERE Date = (SELECT Date FROM Sales WHERE SaleID = NEW.SaleID);

    -- Update SalesTrend based on the values in the temporary table
    INSERT INTO SalesTrend (Date, TotalSales, TotalQuantitySold, AverageSaleAmount, TotalCustomers)
    SELECT
        temp_results1.Date,
        temp_results1.TotalSales,
        temp_results1.TotalQuantitySold,
        temp_results1.AverageSaleAmount,
        temp_results1.TotalCustomers
    FROM temp_results1
    ON DUPLICATE KEY UPDATE
                         TotalSales = VALUES(TotalSales),
                         TotalQuantitySold = VALUES(TotalQuantitySold),
                         AverageSaleAmount = VALUES(AverageSaleAmount),
                         TotalCustomers = VALUES(TotalCustomers);

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS temp_results1;

    -- Temporary table to store intermediate results
    CREATE TEMPORARY TABLE temp_results2 (
                                            Date DATE,
                                            RepeatCustomers INT
    );

    -- Check if the customer is a repeat customer
    INSERT INTO temp_results2 (Date, RepeatCustomers)
    SELECT NEW.Date, 1
    FROM Sales
    WHERE CustomerID = NEW.CustomerID AND Date < NEW.Date
    LIMIT 1;

    -- Increment RepeatCustomers for the corresponding date in SalesTrend
    INSERT INTO SalesTrend (Date, RepeatCustomers)
    VALUES (NEW.Date, COALESCE((SELECT RepeatCustomers + 1 FROM temp_results2), 0))
    ON DUPLICATE KEY UPDATE RepeatCustomers = RepeatCustomers + COALESCE((SELECT RepeatCustomers FROM temp_results2), 0);

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS temp_results2;

-- Temporary table to store intermediate results
    CREATE TEMPORARY TABLE temp_results3 (
                                            Date DATE,
                                            ProductID INT,
                                            ProductPopularity VARCHAR(255)
    );

    -- Update ProductPopularity for the corresponding product
    INSERT INTO temp_results3 (Date, ProductID, ProductPopularity)
    VALUES (NEW.Date, NEW.ProductID, CONCAT(NEW.ProductID, ':', 1))
    ON DUPLICATE KEY UPDATE
        ProductPopularity = CONCAT(NEW.ProductID, ':', SUBSTRING_INDEX(ProductPopularity, ':', -1) + 1);

    -- Update SalesTrend based on the values in the temporary table
    INSERT INTO SalesTrend (Date, ProductPopularity)
    SELECT
        temp_results3.Date,
        temp_results3.ProductPopularity
    FROM temp_results3
    ON DUPLICATE KEY UPDATE ProductPopularity = (SELECT ProductPopularity from temp_results3);

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS temp_results3;

    -- Temporary table to store intermediate results
    CREATE TEMPORARY TABLE temp_results4 (
                                            Date DATE,
                                            SalesGrowthPercentage DECIMAL(5,2)
    );

    -- Update SalesGrowthPercentage for the corresponding date
    INSERT INTO temp_results4 (Date, SalesGrowthPercentage)
    SELECT NEW.Date, IFNULL(
                ((NEW.Amount - LAG(TotalSales) OVER (ORDER BY Date)) / LAG(TotalSales) OVER (ORDER BY Date)) * 100,
                0
                     )
    FROM SalesTrend
    WHERE Date = NEW.Date;

    -- Update SalesTrend based on the values in the temporary table
    INSERT INTO SalesTrend (Date, SalesGrowthPercentage)
    SELECT
        temp_results4.Date,
        temp_results4.SalesGrowthPercentage
   FROM temp_results4
    ON DUPLICATE KEY UPDATE SalesGrowthPercentage = (SELECT SalesGrowthPercentage FROM temp_results4);

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS temp_results4;

    -- Temporary table to store intermediate results
    CREATE TEMPORARY TABLE temp_results5 (
                                            Date DATE,
                                            AveragePurchaseFrequency DECIMAL(5,2)
    );

    -- Update AveragePurchaseFrequency for the corresponding date
    INSERT INTO temp_results5 (Date, AveragePurchaseFrequency)
    SELECT NEW.Date, IFNULL(
            AVG(DATEDIFF(Date, LAG(Date) OVER (PARTITION BY CustomerID ORDER BY Date))),
            0
                     )
    FROM Sales
    WHERE CustomerID = NEW.CustomerID;

    -- Update SalesTrend based on the values in the temporary table
    INSERT INTO SalesTrend (Date, AveragePurchaseFrequency)
    SELECT
        temp_results5.Date,
        temp_results5.AveragePurchaseFrequency
    FROM temp_results5
    ON DUPLICATE KEY UPDATE AveragePurchaseFrequency = (SELECT AveragePurchaseFrequency from temp_results5);

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS temp_results5;

    -- Temporary table to store intermediate results
    CREATE TEMPORARY TABLE temp_results6 (
                                            Date DATE,
                                            CustomerRetentionRate DECIMAL(5,2)
    );

    -- Update CustomerRetentionRate for the corresponding date
    INSERT INTO temp_results6 (Date, CustomerRetentionRate)
    SELECT NEW.Date, IFNULL(
                (COUNT(DISTINCT CASE WHEN Date = NEW.Date THEN CustomerID END) / NULLIF(COUNT(DISTINCT CASE WHEN Date < NEW.Date THEN CustomerID END), 0)) * 100,
                0
                     )
    FROM Sales;

    -- Update SalesTrend based on the values in the temporary table
    INSERT INTO SalesTrend (Date, CustomerRetentionRate)
    SELECT
        temp_results6.Date,
        temp_results6.CustomerRetentionRate
    FROM temp_results6
    ON DUPLICATE KEY UPDATE CustomerRetentionRate = (SELECT CustomerRetentionRate from temp_results6);

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS temp_results6;

    -- Temporary table to store intermediate results
    CREATE TEMPORARY TABLE temp_results7 (
                                            Date DATE,
                                            PromotionEffectiveness DECIMAL(5,2)
    );

    -- Update PromotionEffectiveness for the corresponding date
    INSERT INTO temp_results7 (Date, PromotionEffectiveness)
    SELECT NEW.Date, IFNULL(
            ((SUM(NEW.Amount) - SUM(NEW.Amount * (1 - IFNULL(Promotions.DiscountPercentage, 0) / 100))) / NULLIF(SUM(NEW.Quantity), 0)),
            0
                     )
    FROM Sales
             LEFT JOIN Promotions ON Sales.PromotionID = Promotions.PromotionID
    WHERE Date = NEW.Date;

    -- Update SalesTrend based on the values in the temporary table
    INSERT INTO SalesTrend (Date, PromotionEffectiveness)
    SELECT
        temp_results7.Date,
        temp_results7.PromotionEffectiveness
    FROM temp_results7
    ON DUPLICATE KEY UPDATE PromotionEffectiveness = (SELECT PromotionEffectiveness from temp_results7);

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS temp_results7;
END //

DELIMITER ;

