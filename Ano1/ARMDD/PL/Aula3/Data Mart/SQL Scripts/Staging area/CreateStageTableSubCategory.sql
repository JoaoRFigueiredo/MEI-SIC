If not exists (select name from sys.tables where name = 'SubCategory')
CREATE TABLE [dbo].[SubCategory]
(
	[SubCategoryCode] [char](5),
	[SubCategDescrip] [nvarchar](50)
)
else
truncate table SubCategory
