
*****************  Deploying Packages Tutorial  ***************************

In the Deploying Packages tutorial, you will learn how to use the tools that Integration Services 
provides to install packages and their dependencies on a different computer. 

First you will perform tasks to prepare for deployment. You will create a new Integration Service 
project in Business Intelligence Development Studio and add to the project the existing packages, 
sample packages, and data files that ship with the April, 2006 Web refresh of Books Online. 

You will update the packages to use configurations. The tutorial teaches you how to use a 
combination of environment variables and XML configuration files to implement the configurations. 
After you have verified that the packages run successfully in Business Intelligence Development 
Studio, you will create the deployment bundle for use in installing the packages on another 
computer. The deployment bundle will consist of all files required for the items that you added to 
the Integration Services project, package dependencies, and the deployment utility that you built. 

You will then copy the deployment bundle to the destination computer and run the Package 
Installation Wizard to install the packages and package dependencies. The packages will be 
installed in the msdb SQL Server database; the supporting files will be installed in the file 
system. Because the deployed packages use configurations, you will update the configuration to use 
values that enable packages to run successfully in the new environment. 
Finally, you will run the packages in SQL Server Management Studio by using the Execute Package 
Utility. 

The Books Online topic "Deploying Packages Tutorial" is the topic that begins this tutorial.
To see other tutorials  for Integration Services in Books Online, see the topic "Integration 
Services Tutorials".
