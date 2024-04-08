If not exists (select name from sys.tables where name = 'DimItem')
begin
CREATE TABLE DimItem (
    ItemKey INT IDENTITY(1,1) PRIMARY KEY,
    ItemID CHAR(11) NOT NULL,
    ItemDescription NVARCHAR(50) NOT NULL,
    CategDescription NVARCHAR(50) NOT NULL,
    SubCategDescrip NVARCHAR(50) NOT NULL,
    BrandDescription NVARCHAR(50) NOT NULL,
    UpmarketFlag CHAR(1) NOT NULL,
    EffectiveDate DATETIME NOT NULL,
    ExpiredDate DATETIME,
    IsCurrent NVARCHAR(3) NOT NULL
)
CREATE NONCLUSTERED INDEX [NonClusteredIndex-DimItem] ON [dbo].[DimItem]
(
	[ItemID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
end

