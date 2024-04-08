if not exists (select name from sys.tables where name = 'MaritalStatusDescription_lookup')
begin

CREATE TABLE [dbo].[MaritalStatusDescription_Lookup](
	[MaritalStatus] [nchar](1) NULL,
	[MaritalStatusDescription] [nvarchar](10) NOT NULL
) ON [PRIMARY]

INSERT [dbo].[MaritalStatusDescription_Lookup] ([MaritalStatus], [MaritalStatusDescription]) VALUES (NULL, N'Unknown')
INSERT [dbo].[MaritalStatusDescription_Lookup] ([MaritalStatus], [MaritalStatusDescription]) VALUES (N'S', N'Single')
INSERT [dbo].[MaritalStatusDescription_Lookup] ([MaritalStatus], [MaritalStatusDescription]) VALUES (N'M', N'Married')
INSERT [dbo].[MaritalStatusDescription_Lookup] ([MaritalStatus], [MaritalStatusDescription]) VALUES (N'D', N'Divorced')
INSERT [dbo].[MaritalStatusDescription_Lookup] ([MaritalStatus], [MaritalStatusDescription]) VALUES (N'W', N'Widowed')
end