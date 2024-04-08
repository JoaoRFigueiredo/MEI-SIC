IF NOT EXISTS (SELECT name from sys.tables WHERE name = 'FactCurrencyRatesDQP')
    CREATE TABLE [dbo].[FactCurrencyRatesDQP](
        [CurrencyRateDate] [date] NULL,
        [FromCurrencyKey] [int] NULL,
        [ToCurrencyKey] [int] NULL,
        [AverageRate] [money] NULL,
        [EndOfDayRate] [money] NULL,
        DQP nvarchar(100)
    )
ELSE
    TRUNCATE TABLE FactCurrencyRatesDQP