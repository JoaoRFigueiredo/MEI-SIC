If not exists (select name from sys.tables where name = 'Transaction_Item')
CREATE TABLE [dbo].[Transaction_Item]
(
	[Store] [char](5),
	[Date] [datetime],
	[Time] [int],
	[TransactionID] [char](9),
	[ItemNumber] [tinyint],
	[ItemCode] [char](11),
	[Amount] [money]
)
else 
truncate table Transaction_Item
