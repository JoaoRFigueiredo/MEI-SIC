if not exists (select name from sys.tables where name = 'SalesOrderDetails')

CREATE TABLE [dbo].[SalesOrderDetails](
	[SalesOrderID] [int] NOT NULL,
	[SalesOrderDetailID] [int] NOT NULL,
	[OrderQty] [smallint] NOT NULL,
	[ProductNumber] [nvarchar](25) NOT NULL,
	[UnitPrice] [money] NOT NULL,
	[UnitPriceDiscount] [money] NOT NULL,
	[LineTotal] [numeric](38, 6) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL
)
else
    truncate table SalesOrderDetails