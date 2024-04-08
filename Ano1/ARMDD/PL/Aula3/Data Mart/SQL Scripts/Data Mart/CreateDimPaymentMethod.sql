If not exists (select name from sys.tables where name = 'DimPaymentMethod')
CREATE TABLE DimPaymentMethod (
    PaymentMethodKey INT IDENTITY(1,1) PRIMARY KEY,
    PaymentMethod CHAR(2) NOT NULL,
    PaymentMethodDescription NVARCHAR(20)
)
