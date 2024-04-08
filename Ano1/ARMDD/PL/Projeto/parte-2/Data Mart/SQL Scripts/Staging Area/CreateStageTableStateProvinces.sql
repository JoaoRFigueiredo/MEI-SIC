if not exists (select name from sys.tables where name = 'StateProvinces')

CREATE TABLE [dbo].[StateProvinces](
	[StateProvinceID] [int] NOT NULL,
	[StateProvinceCode] [nchar](3) NOT NULL,
	[CountryRegionCode] [nvarchar](3) NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL
)
else
    truncate table StateProvinces