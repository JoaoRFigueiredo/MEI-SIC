If not exists (select name from sys.tables where name = 'DimCard')
begin
CREATE TABLE DimCard (
    CardKey INT IDENTITY(1,1) PRIMARY KEY,
    CardID CHAR(11) NOT NULL,
    City NVARCHAR(50) NOT NULL,
    Region NVARCHAR(50) NOT NULL,
    PostalCode NVARCHAR(10) NOT NULL,
    CardStartDateKey INT NOT NULL,
    Gender NVARCHAR(6) NOT NULL,
    DateOfBirthKey INT NOT NULL,
    MaritalStatus NVARCHAR(10) NOT NULL,
    NumChildren TINYINT NOT NULL,
    YoungestChildren TINYINT NOT NULL,
    EffectiveDate DATETIME NOT NULL,
    ExpiredDate DATETIME,
    IsCurrent NVARCHAR(3) NOT NULL
)


CREATE NONCLUSTERED INDEX [NonClusteredIndex-CardID] ON [dbo].[DimCard]
(
	[CardID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF)
end