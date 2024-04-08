If not exists (select name from sys.tables where name = 'Item')
CREATE TABLE [dbo].[Item]
(
	[ItemCode] [char](11),
	[ItemDescription] [nvarchar](50),
	[CategoryCode] [char](4),
	[SubCategoryCode] [char](5),
	[BrandCode] [char](9),
	[UpmarketFlag] [char](1)
)
else
truncate table Item
