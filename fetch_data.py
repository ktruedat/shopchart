from dbconnection import create_connection


def fetch_sale_trends_data():
    sales_trends_query = """
        SELECT
            SalesTrendID,
            Date,
            TotalSales,
            TotalQuantitySold,
            AverageSaleAmount,
            TotalCustomers,
            NewCustomers,
            RepeatCustomers,
            ProductPopularity,
            CategoryPopularity,
            SalesGrowthPercentage,
            AveragePurchaseFrequency,
            CustomerRetentionRate,
            SeasonalTrends,
            PromotionEffectiveness
        FROM SalesTrend;
    """
    conn = create_connection()

    # Execute the SQL query using execute method
    result = conn.query(sales_trends_query)

    # Check if the query was successful
    # if result is not None:
    #     # Convert the result to a DataFrame for further processing or display
    #     df = pd.DataFrame(result.fetchall(), columns=result.keys())
    #     st.table(df)
    # else:
    #     st.error("Error executing SQL query.")

    return result
