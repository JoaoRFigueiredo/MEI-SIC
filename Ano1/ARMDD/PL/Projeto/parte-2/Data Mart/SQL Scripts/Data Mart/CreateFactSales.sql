IF NOT EXISTS (SELECT name FROM sys.tables WHERE name = 'FactSales')
BEGIN
    CREATE TABLE [dbo].[FactSales](
		[TerritoryKey] [int] NOT NULL,
		[ShipToAddressKey] [int] NOT NULL,
		[BillToAddressKey] [int] NOT NULL,
		[OrderDateKey] [int] NOT NULL,
		[DueDateKey] [int] NOT NULL,
		[ShipDateKey] [int] NOT NULL,
		[CurrencyKey] [int] NOT NULL,
		[CustomerKey] [int] NOT NULL,
		[EmployeeKey] [int] NOT NULL,
		[ProductKey] [int] NOT NULL,
		[ShippingMethodKey] [int] NOT NULL,
        [SalesOrderDetailID] [int] NOT NULL,
        [SalesOrderID] [int] NOT NULL,
        [OrderQty] [smallint] NOT NULL,
        [UnitPriceLocal] [money] NOT NULL,
        [UnitPriceStandard] [money] NOT NULL,
        [UnitPriceDiscountLocal] [money] NOT NULL,
        [UnitPriceDiscountStandard] [money] NOT NULL,
        [LineTotalLocal] [numeric] (38,6) NOT NULL,
        [LineTotalStandard] [numeric] (38,6) NOT NULL,
		[TaxAmountLocal] [money] NOT NULL,
        [TaxAmountStandard] [money] NOT NULL,
		[FreightLocal] [money] NOT NULL,
        [FreightStandard] [money] NOT NULL,
        [TotalDueLocal] [money] NOT NULL,
        [TotalDueStandard] [money] NOT NULL,
        [SubTotalLocal] [money] NOT NULL,
        [SubTotalStandard] [money] NOT NULL 
        CONSTRAINT [PK_FactSales] PRIMARY KEY CLUSTERED 
        (
            [ProductKey] ASC,
            [OrderDateKey] ASC,
            [CustomerKey] ASC
        ) ON [PRIMARY]
    ) ON [PRIMARY]
END;