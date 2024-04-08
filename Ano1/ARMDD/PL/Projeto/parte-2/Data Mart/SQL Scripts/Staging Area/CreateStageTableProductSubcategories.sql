if not exists (select name from sys.tables where name = 'ProductSubcategories')

CREATE TABLE [dbo].[ProductSubcategories](
	[ProductSubcategoryID] [int] NOT NULL,
	[ProductCategoryID] [int] NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL
)
else
    truncate table ProductSubcategories