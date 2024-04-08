IF NOT EXISTS (SELECT name from sys.tables WHERE name = 'FactSalesDQP')
    CREATE TABLE [dbo].[FactSalesDQP](
        [UnitPriceDiscountLocal] [money] NULL,
        [TotalDueLocal] [money] NULL,
        [SalesOrderID] [int] NULL,
        [TaxAmountLocal] [money] NULL,
        [LineTotalStandard] [numeric] (38,6) NULL,
        [TerritoryID] [int] NULL,
        [OrderQty] [smallint] NULL,
        [SubTotalLocal] [money] NULL,
        [BillToAddress] [int] NULL,
        [ShipToAddress] [int] NULL,
        [OrderDate] [date] NULL,
        [DueDate] [date] NULL,
        [CustomerID] [int] NULL,
        [UnitPriceDiscountStandard] [money] NULL,
        [BusinessEntityID] [int] NULL,
        [CurrencyCode] [nchar](3) NULL,
        [FreightLocal] [money] NULL,
        [LineTotalLocal] [numeric] (38,6) NULL,
        [FreightStandard] [money] NULL,
        [ShipMethodID] [int] NULL,
        [ProductNumber] [nvarchar](25),
        [SubTotalStandard] [money] NULL,
        [UnitPriceLocal] [money] NULL,
        [ShipDate] [date] NULL,
        [UnitPriceStandard] [money] NULL,
        [TotalDueStandard] [money] NULL,
        [TaxAmountStandard] [money] NULL,
        [SalesOrderDetailID] [int] NULL,
        [DQP] nvarchar(100)
    )
ELSE
    TRUNCATE TABLE FactSalesDQP
