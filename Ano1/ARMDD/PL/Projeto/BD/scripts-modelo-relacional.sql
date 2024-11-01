USE [Bikes&Bikes]
GO
/****** Object:  Table [dbo].[Addresses]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Addresses](
	[AddressID] [int] NOT NULL,
	[AddressLine1] [nvarchar](60) NOT NULL,
	[AddressLine2] [nvarchar](60) NULL,
	[City] [nvarchar](30) NOT NULL,
	[StateProvinceID] [int] NOT NULL,
	[PostalCode] [nvarchar](15) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_Address_AddressID] PRIMARY KEY CLUSTERED 
(
	[AddressID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CountryRegions]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CountryRegions](
	[CountryRegionCode] [nvarchar](3) NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_CountryRegion_CountryRegionCode] PRIMARY KEY CLUSTERED 
(
	[CountryRegionCode] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Currencies]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Currencies](
	[CurrencyCode] [nchar](3) NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_Currency_CurrencyCode] PRIMARY KEY CLUSTERED 
(
	[CurrencyCode] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CurrencyRates]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CurrencyRates](
	[CurrencyRateID] [int] NOT NULL,
	[CurrencyRateDate] [date] NOT NULL,
	[FromCurrencyCode] [nchar](3) NOT NULL,
	[ToCurrencyCode] [nchar](3) NOT NULL,
	[AverageRate] [money] NOT NULL,
	[EndOfDayRate] [money] NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_CurrencyRate_CurrencyRateID] PRIMARY KEY CLUSTERED 
(
	[CurrencyRateID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Customers]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Customers](
	[CustomerID] [int] NOT NULL,
	[PersonID] [int] NULL,
	[CreatedDate] [date] NULL,
	[ModifiedDate] [date] NULL,
 CONSTRAINT [PK_Customer_CustomerID] PRIMARY KEY CLUSTERED 
(
	[CustomerID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Employees]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Employees](
	[BusinessEntityID] [int] NOT NULL,
	[NationalIDNumber] [nvarchar](15) NOT NULL,
	[LoginID] [nvarchar](256) NOT NULL,
	[JobTitle] [nvarchar](50) NOT NULL,
	[BirthDate] [date] NOT NULL,
	[MaritalStatus] [nchar](1) NOT NULL,
	[Gender] [nchar](1) NOT NULL,
	[HireDate] [date] NOT NULL,
	[SalariedFlag] [bit] NOT NULL,
	[VacationHours] [smallint] NOT NULL,
	[SickLeaveHours] [smallint] NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_Employee_BusinessEntityID] PRIMARY KEY CLUSTERED 
(
	[BusinessEntityID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Persons]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Persons](
	[BusinessEntityID] [int] NOT NULL,
	[PersonType] [nvarchar](20) NOT NULL,
	[Title] [nvarchar](8) NULL,
	[FirstName] [nvarchar](50) NOT NULL,
	[MiddleName] [nvarchar](50) NULL,
	[LastName] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_Person_BusinessEntityID] PRIMARY KEY CLUSTERED 
(
	[BusinessEntityID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ProductCategories]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ProductCategories](
	[ProductCategoryID] [int] NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_ProductCategory_ProductCategoryID] PRIMARY KEY CLUSTERED 
(
	[ProductCategoryID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Products]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Products](
	[ProductNumber] [nvarchar](25) NOT NULL,
	[Name] [nvarchar](50) NULL,
	[FinishedGoodsFlag] [bit] NULL,
	[Color] [nvarchar](15) NULL,
	[SafetyStockLevel] [smallint] NULL,
	[ReorderPoint] [smallint] NULL,
	[StandardCost] [money] NULL,
	[ListPrice] [money] NULL,
	[Size] [nvarchar](5) NULL,
	[SizeUnitMeasureCode] [nchar](3) NULL,
	[Weight] [decimal](8, 2) NULL,
	[WeightUnitMeasureCode] [nchar](3) NULL,
	[DaysToManufacture] [int] NULL,
	[ProductLine] [nvarchar](10) NULL,
	[Class] [nvarchar](10) NULL,
	[Style] [nvarchar](10) NULL,
	[ProductSubcategoryID] [int] NULL,
	[SellStartDate] [date] NULL,
	[SellEndDate] [date] NULL,
	[CreatedDate] [date] NULL,
	[ModifiedDate] [date] NULL,
 CONSTRAINT [PK_Products] PRIMARY KEY CLUSTERED 
(
	[ProductNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ProductSubcategories]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ProductSubcategories](
	[ProductSubcategoryID] [int] NOT NULL,
	[ProductCategoryID] [int] NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_ProductSubcategory_ProductSubcategoryID] PRIMARY KEY CLUSTERED 
(
	[ProductSubcategoryID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SalesOrderDetails]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SalesOrderDetails](
	[SalesOrderID] [int] NOT NULL,
	[SalesOrderDetailID] [int] NOT NULL,
	[OrderQty] [smallint] NOT NULL,
	[ProductNumber] [nvarchar](25) NOT NULL,
	[UnitPrice] [money] NOT NULL,
	[UnitPriceDiscount] [money] NOT NULL,
	[LineTotal] [numeric](38, 6) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_SalesOrderDetail] PRIMARY KEY CLUSTERED 
(
	[SalesOrderID] ASC,
	[SalesOrderDetailID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SalesOrderHeaders]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SalesOrderHeaders](
	[SalesOrderID] [int] NOT NULL,
	[OrderDate] [date] NOT NULL,
	[DueDate] [date] NOT NULL,
	[ShipDate] [date] NOT NULL,
	[CustomerID] [int] NOT NULL,
	[SalesPersonID] [int] NULL,
	[TerritoryID] [int] NOT NULL,
	[BillToAddressID] [int] NOT NULL,
	[ShipToAddressID] [int] NOT NULL,
	[ShipMethodID] [int] NOT NULL,
	[CurrencyCode] [nchar](3) NULL,
	[SubTotal] [money] NOT NULL,
	[TaxAmount] [money] NOT NULL,
	[Freight] [money] NOT NULL,
	[TotalDue] [money] NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_SalesOrderHeader] PRIMARY KEY CLUSTERED 
(
	[SalesOrderID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SalesPersons]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SalesPersons](
	[BusinessEntityID] [int] NOT NULL,
	[SalesQuota] [money] NULL,
	[Bonus] [money] NOT NULL,
	[CommissionPct] [smallmoney] NOT NULL,
	[SalesYTD] [money] NOT NULL,
	[SalesLastYear] [money] NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_SalesPerson_BusinessEntityID] PRIMARY KEY CLUSTERED 
(
	[BusinessEntityID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SalesTerritories]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SalesTerritories](
	[TerritoryID] [int] NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CountryRegionCode] [nvarchar](3) NOT NULL,
	[Group] [nvarchar](50) NOT NULL,
	[SalesYTD] [money] NOT NULL,
	[SalesLastYear] [money] NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_SalesTerritory_TerritoryID] PRIMARY KEY CLUSTERED 
(
	[TerritoryID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ShipMethods]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ShipMethods](
	[ShipMethodID] [int] NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[ShipBase] [money] NOT NULL,
	[ShipRate] [money] NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_ShipMethod_ShipMethodID] PRIMARY KEY CLUSTERED 
(
	[ShipMethodID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[StateProvinces]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[StateProvinces](
	[StateProvinceID] [int] NOT NULL,
	[StateProvinceCode] [nchar](3) NOT NULL,
	[CountryRegionCode] [nvarchar](3) NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_StateProvince_StateProvinceID] PRIMARY KEY CLUSTERED 
(
	[StateProvinceID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[UnitMeasures]    Script Date: 30/11/2023 20:04:56 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[UnitMeasures](
	[UnitMeasureCode] [nchar](3) NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[CreatedDate] [date] NOT NULL,
	[ModifiedDate] [date] NOT NULL,
 CONSTRAINT [PK_UnitMeasure_UnitMeasureCode] PRIMARY KEY CLUSTERED 
(
	[UnitMeasureCode] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Addresses]  WITH CHECK ADD  CONSTRAINT [FK_Address_StateProvince] FOREIGN KEY([StateProvinceID])
REFERENCES [dbo].[StateProvinces] ([StateProvinceID])
GO
ALTER TABLE [dbo].[Addresses] CHECK CONSTRAINT [FK_Address_StateProvince]
GO
ALTER TABLE [dbo].[CurrencyRates]  WITH CHECK ADD  CONSTRAINT [FK_CurrencyRate_Currency] FOREIGN KEY([ToCurrencyCode])
REFERENCES [dbo].[Currencies] ([CurrencyCode])
GO
ALTER TABLE [dbo].[CurrencyRates] CHECK CONSTRAINT [FK_CurrencyRate_Currency]
GO
ALTER TABLE [dbo].[CurrencyRates]  WITH CHECK ADD  CONSTRAINT [FK_CurrencyRate_Currency1] FOREIGN KEY([FromCurrencyCode])
REFERENCES [dbo].[Currencies] ([CurrencyCode])
GO
ALTER TABLE [dbo].[CurrencyRates] CHECK CONSTRAINT [FK_CurrencyRate_Currency1]
GO
ALTER TABLE [dbo].[Customers]  WITH CHECK ADD  CONSTRAINT [FK_Customers_Persons] FOREIGN KEY([PersonID])
REFERENCES [dbo].[Persons] ([BusinessEntityID])
GO
ALTER TABLE [dbo].[Customers] CHECK CONSTRAINT [FK_Customers_Persons]
GO
ALTER TABLE [dbo].[Employees]  WITH CHECK ADD  CONSTRAINT [FK_Employee_Person] FOREIGN KEY([BusinessEntityID])
REFERENCES [dbo].[Persons] ([BusinessEntityID])
GO
ALTER TABLE [dbo].[Employees] CHECK CONSTRAINT [FK_Employee_Person]
GO
ALTER TABLE [dbo].[Products]  WITH CHECK ADD  CONSTRAINT [FK_Product_ProductSubcategory] FOREIGN KEY([ProductSubcategoryID])
REFERENCES [dbo].[ProductSubcategories] ([ProductSubcategoryID])
GO
ALTER TABLE [dbo].[Products] CHECK CONSTRAINT [FK_Product_ProductSubcategory]
GO
ALTER TABLE [dbo].[Products]  WITH CHECK ADD  CONSTRAINT [FK_Product_UnitMeasure] FOREIGN KEY([SizeUnitMeasureCode])
REFERENCES [dbo].[UnitMeasures] ([UnitMeasureCode])
GO
ALTER TABLE [dbo].[Products] CHECK CONSTRAINT [FK_Product_UnitMeasure]
GO
ALTER TABLE [dbo].[Products]  WITH CHECK ADD  CONSTRAINT [FK_Product_UnitMeasure1] FOREIGN KEY([WeightUnitMeasureCode])
REFERENCES [dbo].[UnitMeasures] ([UnitMeasureCode])
GO
ALTER TABLE [dbo].[Products] CHECK CONSTRAINT [FK_Product_UnitMeasure1]
GO
ALTER TABLE [dbo].[ProductSubcategories]  WITH CHECK ADD  CONSTRAINT [FK_ProductSubcategory_ProductCategory] FOREIGN KEY([ProductCategoryID])
REFERENCES [dbo].[ProductCategories] ([ProductCategoryID])
GO
ALTER TABLE [dbo].[ProductSubcategories] CHECK CONSTRAINT [FK_ProductSubcategory_ProductCategory]
GO
ALTER TABLE [dbo].[SalesOrderDetails]  WITH CHECK ADD  CONSTRAINT [FK_SalesOrderDetail_SalesOrderHeader] FOREIGN KEY([SalesOrderID])
REFERENCES [dbo].[SalesOrderHeaders] ([SalesOrderID])
GO
ALTER TABLE [dbo].[SalesOrderDetails] CHECK CONSTRAINT [FK_SalesOrderDetail_SalesOrderHeader]
GO
ALTER TABLE [dbo].[SalesOrderDetails]  WITH CHECK ADD  CONSTRAINT [FK_SalesOrderDetails_Products] FOREIGN KEY([ProductNumber])
REFERENCES [dbo].[Products] ([ProductNumber])
GO
ALTER TABLE [dbo].[SalesOrderDetails] CHECK CONSTRAINT [FK_SalesOrderDetails_Products]
GO
ALTER TABLE [dbo].[SalesOrderHeaders]  WITH CHECK ADD  CONSTRAINT [FK_SalesOrderHeader_Address] FOREIGN KEY([ShipToAddressID])
REFERENCES [dbo].[Addresses] ([AddressID])
GO
ALTER TABLE [dbo].[SalesOrderHeaders] CHECK CONSTRAINT [FK_SalesOrderHeader_Address]
GO
ALTER TABLE [dbo].[SalesOrderHeaders]  WITH CHECK ADD  CONSTRAINT [FK_SalesOrderHeader_Address1] FOREIGN KEY([BillToAddressID])
REFERENCES [dbo].[Addresses] ([AddressID])
GO
ALTER TABLE [dbo].[SalesOrderHeaders] CHECK CONSTRAINT [FK_SalesOrderHeader_Address1]
GO
ALTER TABLE [dbo].[SalesOrderHeaders]  WITH CHECK ADD  CONSTRAINT [FK_SalesOrderHeader_Currency] FOREIGN KEY([CurrencyCode])
REFERENCES [dbo].[Currencies] ([CurrencyCode])
GO
ALTER TABLE [dbo].[SalesOrderHeaders] CHECK CONSTRAINT [FK_SalesOrderHeader_Currency]
GO
ALTER TABLE [dbo].[SalesOrderHeaders]  WITH CHECK ADD  CONSTRAINT [FK_SalesOrderHeader_Customer] FOREIGN KEY([CustomerID])
REFERENCES [dbo].[Customers] ([CustomerID])
GO
ALTER TABLE [dbo].[SalesOrderHeaders] CHECK CONSTRAINT [FK_SalesOrderHeader_Customer]
GO
ALTER TABLE [dbo].[SalesOrderHeaders]  WITH CHECK ADD  CONSTRAINT [FK_SalesOrderHeader_SalesPerson] FOREIGN KEY([SalesPersonID])
REFERENCES [dbo].[SalesPersons] ([BusinessEntityID])
GO
ALTER TABLE [dbo].[SalesOrderHeaders] CHECK CONSTRAINT [FK_SalesOrderHeader_SalesPerson]
GO
ALTER TABLE [dbo].[SalesOrderHeaders]  WITH CHECK ADD  CONSTRAINT [FK_SalesOrderHeader_SalesTerritory] FOREIGN KEY([TerritoryID])
REFERENCES [dbo].[SalesTerritories] ([TerritoryID])
GO
ALTER TABLE [dbo].[SalesOrderHeaders] CHECK CONSTRAINT [FK_SalesOrderHeader_SalesTerritory]
GO
ALTER TABLE [dbo].[SalesOrderHeaders]  WITH CHECK ADD  CONSTRAINT [FK_SalesOrderHeader_ShipMethod] FOREIGN KEY([ShipMethodID])
REFERENCES [dbo].[ShipMethods] ([ShipMethodID])
GO
ALTER TABLE [dbo].[SalesOrderHeaders] CHECK CONSTRAINT [FK_SalesOrderHeader_ShipMethod]
GO
ALTER TABLE [dbo].[SalesPersons]  WITH CHECK ADD  CONSTRAINT [FK_SalesPerson_Employee] FOREIGN KEY([BusinessEntityID])
REFERENCES [dbo].[Employees] ([BusinessEntityID])
GO
ALTER TABLE [dbo].[SalesPersons] CHECK CONSTRAINT [FK_SalesPerson_Employee]
GO
ALTER TABLE [dbo].[SalesTerritories]  WITH CHECK ADD  CONSTRAINT [FK_SalesTerritory_CountryRegion] FOREIGN KEY([CountryRegionCode])
REFERENCES [dbo].[CountryRegions] ([CountryRegionCode])
GO
ALTER TABLE [dbo].[SalesTerritories] CHECK CONSTRAINT [FK_SalesTerritory_CountryRegion]
GO
ALTER TABLE [dbo].[StateProvinces]  WITH CHECK ADD  CONSTRAINT [FK_StateProvince_CountryRegion] FOREIGN KEY([CountryRegionCode])
REFERENCES [dbo].[CountryRegions] ([CountryRegionCode])
GO
ALTER TABLE [dbo].[StateProvinces] CHECK CONSTRAINT [FK_StateProvince_CountryRegion]
GO
