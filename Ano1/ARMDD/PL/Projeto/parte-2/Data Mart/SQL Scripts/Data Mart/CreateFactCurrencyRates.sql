IF NOT EXISTS (SELECT name FROM sys.tables WHERE name = 'FactCurrencyRates')
	CREATE TABLE [dbo].[FactCurrencyRates](
		[DateKey] [int] NOT NULL,
		[ToCurrencyKey] [int] NOT NULL,
		[FromCurrencyKey] [int] NOT NULL,
		[AverageRate] [money] NOT NULL,
		[EndOfDayRate] [money] NOT NULL
		
	CONSTRAINT [PK_FactCurrencyRates] PRIMARY KEY CLUSTERED 
	(
		[DateKey] ASC,
		[ToCurrencyKey] ASC,
		[FromCurrencyKey] ASC

	)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
	) ON [PRIMARY]
