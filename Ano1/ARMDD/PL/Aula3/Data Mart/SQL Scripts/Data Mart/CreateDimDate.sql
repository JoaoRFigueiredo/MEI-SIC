If not exists (select name from sys.tables where name = 'DimDate')
CREATE TABLE DimDate (
    DateKey INT IDENTITY(1,1) PRIMARY KEY,
    FullDate DATETIME NOT NULL,
    Year INT NOT NULL,
    Semester TINYINT NOT NULL,
    Quarter TINYINT NOT NULL,
    Month TINYINT NOT NULL,
    MonthName NVARCHAR(10) NOT NULL,
    Week TINYINT NOT NULL,
    DayNumberOfYear INT NOT NULL,
    DayNumberOfMonth TINYINT NOT NULL,
    DayNumberOfWeek TINYINT NOT NULL,
    DayOfWeek NVARCHAR(10) NOT NULL,
    Weekend NVARCHAR(3) NOT NULL
)
