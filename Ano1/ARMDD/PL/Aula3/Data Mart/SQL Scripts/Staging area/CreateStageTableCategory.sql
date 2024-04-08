If not exists (select name from sys.tables where name = 'Category')
CREATE TABLE [dbo].[Category]
(
	[CategoryCode] [char](4),
	[CategDescription] [nvarchar](50)
)
else
truncate Table Category
