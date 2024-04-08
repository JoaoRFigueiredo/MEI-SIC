If not exists (select name from sys.tables where name = 'Card')
CREATE TABLE [dbo].[Card]
(
	[CardID] [char](11),
	[City] [nvarchar](50),
	[Region] [nvarchar](50),
	[PostalCode] [nvarchar](10),
	[CardStartDate] [datetime],
	[Gender] [char](1),
	[DateOfBirth] [datetime],
	[MaritalStatus] [char](1),
	[HasChildren] [char](1),
	[NumChildren] tinyint,
	[YoungestChildren] tinyint
)
else 
truncate table Card
