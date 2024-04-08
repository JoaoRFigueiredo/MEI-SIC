if not exists (select name from sys.tables where name = 'SalesOrderHeaders')

CREATE TABLE [dbo].[SalesOrderHeaders](
	[SalesOrderID] [int] NOT NULL,
	[OrderDate] [date] NOT NULL,
	[DueDate] [date] NOT NULL,
	[ShipDate] [date] NOT NULL,
	[CustomerID] [int] NOT NULL,
	[SalesPersonID] [int] NULL,
	[TerritoryID] [int] NOT NULL,
	[BillToAddressID] [int] NOT NULL,
	[ShipToAddressID] [int] NOT NULL,
	[ShipMethodID] [int] NOT NULL,
	[CurrencyCode] [nchar](3) NULL,
	[SubTotal] [money] NOT NULL,
	[TaxAmount] [money] NOT NULL,
	[Freight] [money] NOT NULL,
	[TotalDue] [money] NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL
)
else
    truncate table SalesOrderHeaders