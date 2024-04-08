if not exists (select name from sys.tables where name = 'Customers')

CREATE TABLE [dbo].[Customers](
	[CustomerID] [int] NOT NULL,
	[PersonID] [int] NULL,
	[CreatedDate] [date] NULL,
	[ModifiedDate] [date] NULL
)
else
    truncate table Customers