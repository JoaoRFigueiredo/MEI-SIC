
if not exists (select name from sys.tables where name = 'CountryRegions')

CREATE TABLE [dbo].[CountryRegions](
	[CountryRegionCode] [nvarchar](3) NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL
)
else
    truncate table CountryRegions