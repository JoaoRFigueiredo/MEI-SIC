if not exists (select name from sys.tables where name = 'ProductCategories')

CREATE TABLE [dbo].[ProductCategories](
	[ProductCategoryID] [int] NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL
)
else
    truncate table ProductCategories