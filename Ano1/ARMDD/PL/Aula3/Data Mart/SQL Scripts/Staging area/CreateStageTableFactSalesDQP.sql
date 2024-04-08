If not exists (select name from sys.tables where name = 'FactSalesDQP')
CREATE TABLE [dbo].[FactSalesDQP]
(
	[Store] [char](5),
	[Date] [datetime],
	[Time] [int],
	[TransactionID] [char](9),
	[CardID] [char](11),
	[PaymentMethod] [char](2),
	[ItemCode] [char](11),
	[Amount] [money],
	DQP nvarchar(100)
)
else 
truncate table FactSalesDQP
