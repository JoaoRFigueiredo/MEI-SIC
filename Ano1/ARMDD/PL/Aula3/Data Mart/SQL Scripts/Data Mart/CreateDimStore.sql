If not exists (select name from sys.tables where name = 'DimStore')
CREATE TABLE DimStore (
    StoreKey INT IDENTITY(1,1) PRIMARY KEY,
    StoreID CHAR(5) NOT NULL,
    StoreName NVARCHAR(20)
)
