IF NOT EXISTS (SELECT name from sys.tables WHERE name = 'DimDate')
BEGIN
	CREATE TABLE [dbo].[DimDate](
		[DateKey] [int] IDENTITY(1,1) NOT NULL,
		[FullDate] [date] NOT NULL,
		[Year] [int] NOT NULL,
		[Semester] [tinyint] NOT NULL,
		[Quarter] [tinyint] NOT NULL,
		[Month] [tinyint] NOT NULL,
		[MonthName] [nvarchar](10) NOT NULL,
		[Week] [tinyint] NOT NULL,
		[DayNumberOfYear] [int] NOT NULL,
		[DayNumberOfMonth] [tinyint] NOT NULL,
		[DayNumberOfWeek] [tinyint] NOT NULL,
		[DayOfWeek] [nvarchar](10) NOT NULL,
		[Weekend] [nvarchar](3) NOT NULL,
		[LastDayOfMonth] [nvarchar](3) NOT NULL,
		[Season] [nvarchar](6) NOT NULL,
		[Trimester] [nvarchar](1) NOT NULL
		CONSTRAINT [PK_DimDate] PRIMARY KEY CLUSTERED 
	(
		[DateKey] ASC
	)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
	) ON [PRIMARY]

CREATE NONCLUSTERED INDEX [NonClusteredIndex-DateKey] ON [dbo].[DimDate]
(
	[DateKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF)
END