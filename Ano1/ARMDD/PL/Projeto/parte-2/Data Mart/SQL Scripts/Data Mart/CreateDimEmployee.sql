IF NOT EXISTS (SELECT name FROM sys.tables WHERE name = 'DimEmployee')
	BEGIN
	CREATE TABLE [dbo].[DimEmployee](
		[EmployeeKey] [int] IDENTITY(1,1) NOT NULL,
		[BusinessEntityID] [int] NOT NULL,
		[SalesQuota] [money] NULL,
		[Bonus] [money] NOT NULL,
		[ComissionPct] [smallmoney] NOT NULL,
		[SalesYTD] [money] NOT NULL,
		[SalesLastYear] [money] NOT NULL,
		[NationalIDNumber] [nvarchar] (15) NOT NULL,
		[LoginID] [nvarchar] (256) NOT NULL,
		[JobTitle] [nvarchar] (50) NOT NULL,
		[BirthDate] [date] NOT NULL,
		[MaritalStatus] [nchar] (10) NOT NULL,
		[Gender] [nchar] (6) NOT NULL,
		[HireDate] [date] NOT NULL,
		[SalariedFlag] [nchar](3) NOT NULL,
		[VacationHours] [smallint] NOT NULL,
		[SickLeaveHours] [smallint] NOT NULL,
		[PersonType] [nvarchar] (20) NOT NULL,
		[Title] [nvarchar] (8) NULL,
		[FirstName] [nvarchar] (50) NOT NULL,
		[MiddleName] [nvarchar] (50)  NULL,
		[LastName] [nvarchar] (50) NOT NULL,
		[CreatedDate] [date] NOT NULL,
		[ModifiedDate] [date]  NULL,
		[EffectiveDate] [datetime] NOT NULL,
		[ExpiredDate] [datetime] NULL,
		[IsCurrent] [nvarchar] (3) NOT NULL
		CONSTRAINT [PK_DimStore] PRIMARY KEY CLUSTERED 
	(
		[EmployeeKey] ASC
	)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
	) ON [PRIMARY]

	CREATE NONCLUSTERED INDEX [NonClusteredIndex-EmployeeKey] ON [dbo].[DimEmployee]
(
	[EmployeeKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF)
END

