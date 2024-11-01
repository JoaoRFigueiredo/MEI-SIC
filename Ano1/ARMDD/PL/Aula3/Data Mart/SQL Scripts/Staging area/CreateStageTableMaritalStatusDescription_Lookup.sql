if not exists (select name from sys.tables where name = 'MaritalStatusDescription_Lookup')
begin
CREATE TABLE [dbo].[MaritalStatusDescription_Lookup](
	[MaritalStatus] [char](1) NULL,
	[MaritalStatusDescription] [nchar](10) NOT NULL
) ON [PRIMARY]

INSERT [dbo].[MaritalStatusDescription_Lookup] ([MaritalStatus], [MaritalStatusDescription]) VALUES (NULL, N'Unknown   ')
INSERT [dbo].[MaritalStatusDescription_Lookup] ([MaritalStatus], [MaritalStatusDescription]) VALUES (N'S', N'Single    ')
INSERT [dbo].[MaritalStatusDescription_Lookup] ([MaritalStatus], [MaritalStatusDescription]) VALUES (N'M', N'Married   ')
INSERT [dbo].[MaritalStatusDescription_Lookup] ([MaritalStatus], [MaritalStatusDescription]) VALUES (N'D', N'Divorced  ')
INSERT [dbo].[MaritalStatusDescription_Lookup] ([MaritalStatus], [MaritalStatusDescription]) VALUES (N'W', N'Widowed   ')
end