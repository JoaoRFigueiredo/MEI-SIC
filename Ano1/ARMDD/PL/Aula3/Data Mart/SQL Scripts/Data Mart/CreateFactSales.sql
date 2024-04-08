If not exists (select name from sys.tables where name = 'FactSales')
CREATE TABLE FactSales (
    DateKey INT NOT NULL,
    TimeKey INT NOT NULL,
    CardKey INT NOT NULL,
    ItemKey INT NOT NULL,
    StoreKey INT NOT NULL,
    PaymentMethodKey INT NOT NULL,
    TransactionID CHAR(9) NOT NULL,
    Quant TINYINT NOT NULL,
    Amount MONEY NOT NULL,
    TotalAmount MONEY NOT NULL,
    PRIMARY KEY (DateKey, TimeKey, CardKey, ItemKey, StoreKey)
)
