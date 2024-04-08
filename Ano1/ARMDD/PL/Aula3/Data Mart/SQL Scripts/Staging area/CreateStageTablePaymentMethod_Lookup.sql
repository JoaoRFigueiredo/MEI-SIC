if not exists (select name from sys.tables where name = 'PaymentMethod_Lookup')
begin
CREATE TABLE [dbo].[PaymentMethod_Lookup](
	[PaymentMethod] [char](2) NOT NULL,
	[PaymentMethodDescription] [nvarchar](20) NOT NULL,
 CONSTRAINT [PK_PaymentMethod_Lookup] PRIMARY KEY CLUSTERED 
(
	[PaymentMethod] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
INSERT [dbo].[PaymentMethod_Lookup] ([PaymentMethod], [PaymentMethodDescription]) VALUES (N'CA', N'Cash Advance')
INSERT [dbo].[PaymentMethod_Lookup] ([PaymentMethod], [PaymentMethodDescription]) VALUES (N'CC', N'Credit Card')
INSERT [dbo].[PaymentMethod_Lookup] ([PaymentMethod], [PaymentMethodDescription]) VALUES (N'CH', N'Check')
INSERT [dbo].[PaymentMethod_Lookup] ([PaymentMethod], [PaymentMethodDescription]) VALUES (N'DC', N'Debit Card')
end