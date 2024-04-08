If not exists (select name from sys.tables where name = 'TransactionDQP')
CREATE TABLE [dbo].[TransactionDQP]
(
	[Store] [char](5),
	[PaymentMethod] [char](2),
	DQP nvarchar (100)
)
else 
truncate table [TransactionDQP]
