If not exists (select name from sys.tables where name = 'Brand')
CREATE TABLE [dbo].[Brand]
(
	[BrandCode] [char](9),
	[BrandDescription] [nvarchar](50)	
)
else
	truncate Table Brand
