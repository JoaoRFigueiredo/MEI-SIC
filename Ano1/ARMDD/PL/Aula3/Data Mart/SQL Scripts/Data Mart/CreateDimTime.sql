If not exists (select name from sys.tables where name = 'DimTime')
CREATE TABLE DimTime (
    TimeKey INT IDENTITY(1,1) PRIMARY KEY,
    FullTime TIME NOT NULL,
    FullTime_int INT NOT NULL,
    Hour TINYINT NOT NULL,
    Minute TINYINT NOT NULL,
    Second TINYINT NOT NULL,
    Period NVARCHAR(10) NOT NULL,
    LunchTime NVARCHAR(3) NOT NULL,
    DinnerTime NVARCHAR(3) NOT NULL
)
