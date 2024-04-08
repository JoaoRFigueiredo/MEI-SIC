if not exists (select name from sys.tables where name = 'CurrencyRates')

CREATE TABLE [dbo].[CurrencyRates](
	[CurrencyRateID] [int] NOT NULL,
	[CurrencyRateDate] [date] NOT NULL,
	[FromCurrencyCode] [nchar](3) NOT NULL,
	[ToCurrencyCode] [nchar](3) NOT NULL,
	[AverageRate] [money] NOT NULL,
	[EndOfDayRate] [money] NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL
)
else
    truncate table CurrencyRates