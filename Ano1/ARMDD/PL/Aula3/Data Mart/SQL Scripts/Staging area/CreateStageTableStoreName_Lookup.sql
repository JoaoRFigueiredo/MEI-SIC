if not exists (select name from sys.tables where name = 'StoreName_Lookup')
begin
CREATE TABLE [dbo].[StoreName_Lookup](
	[StoreID] [char](5) NOT NULL,
	[StoreName] [nchar](20) NOT NULL,
 CONSTRAINT [PK_StoreName_Lookup] PRIMARY KEY CLUSTERED 
(
	[StoreID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
INSERT [dbo].[StoreName_Lookup] ([StoreID], [StoreName]) VALUES (N'S0002', N'Kingsville          ')
INSERT [dbo].[StoreName_Lookup] ([StoreID], [StoreName]) VALUES (N'S0006', N'CatBurg             ')
INSERT [dbo].[StoreName_Lookup] ([StoreID], [StoreName]) VALUES (N'S0015', N'Princeton           ')
INSERT [dbo].[StoreName_Lookup] ([StoreID], [StoreName]) VALUES (N'S0034', N'Queensbury          ')
INSERT [dbo].[StoreName_Lookup] ([StoreID], [StoreName]) VALUES (N'S0040', N'Foxton              ')
INSERT [dbo].[StoreName_Lookup] ([StoreID], [StoreName]) VALUES (N'S0056', N'Ravensmile          ')
end