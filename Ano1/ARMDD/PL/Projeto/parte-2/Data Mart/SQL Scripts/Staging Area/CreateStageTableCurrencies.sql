if not exists (select name from sys.tables where name = 'Currencies')

CREATE TABLE [dbo].[Currencies](
	[CurrencyCode] [nchar](3) NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL
)
else
    truncate table Currencies