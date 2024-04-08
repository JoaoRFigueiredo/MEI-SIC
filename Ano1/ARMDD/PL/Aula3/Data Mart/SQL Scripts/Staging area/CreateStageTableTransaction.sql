If not exists (select name from sys.tables where name = 'Transaction')
CREATE TABLE [dbo].[Transaction]
(
	[Store] [char](5),
	[Date] [datetime],
	[Time] [int],
	[TransactionID] [char](9),
	[CardID] [char](11),
	[PaymentMethod] [char](2)
)
else 
truncate table [Transaction]
