IF NOT EXISTS (SELECT name FROM sys.tables WHERE name = 'DimTerritory')
	BEGIN
	CREATE TABLE [dbo].[DimTerritory](
		[TerritoryKey] [int] IDENTITY(1,1) NOT NULL,
		[TerritoryID] [int] NOT NULL,
		[TerritoryName] [nvarchar](50) NOT NULL,	
		[Group] [nvarchar](50) NOT NULL,	
		[SalesYTD] [money] NOT NULL,
		[SalesLastYear] [money] NOT NULL,
		[CountryRegionName] [nvarchar](50) NOT NULL,	
		[CreatedDate] [date] NOT NULL,	
		[ModifiedDate] [date] NOT NULL,
		[EffectiveDate] [datetime] NOT NULL,	
		[ExpiredDate] [datetime] NULL,
		[IsCurrent] [nvarchar] (3) NOT NULL,	
		CONSTRAINT [PK_DimTerritory] PRIMARY KEY CLUSTERED 
	(
		[TerritoryKey] ASC
	)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
	) ON [PRIMARY]

	CREATE NONCLUSTERED INDEX [NonClusteredIndex-TerritoryKey] ON [dbo].[DimTerritory]
(
	[TerritoryKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF)
END