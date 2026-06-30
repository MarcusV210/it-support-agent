---
source: IBM_TAM_ESSO_TroubleshootingGuide_pdf.pdf
converted: 2026-06-24
---

**==> picture [612 x 159] intentionally omitted <==**

IBM[®] Security Access Manager for Enterprise Single Sign-On Version 8.2 

_Troubleshooting and Support Guide_ 

��� 

**GC23-9693-01** 

**==> picture [612 x 159] intentionally omitted <==**

IBM[®] Security Access Manager for Enterprise Single Sign-On Version 8.2 

_Troubleshooting and Support Guide_ 

## ��� 

**GC23-9693-01** 

## **Note** 

Before using this information and the product it supports, read the information in “Notices” on page 55. 

## **Edition notice** 

**Note: This edition applies to version 8.2 of IBM Security Access Manager for Enterprise Single Sign-On, (product number 5724–V67) and to all subsequent releases and modifications until otherwise indicated in new editions.** 

**© Copyright IBM Corporation 2002, 2012.** 

US Government Users Restricted Rights – Use, duplication or disclosure restricted by GSA ADP Schedule Contract with IBM Corp. 

## **Contents** 

|**About this publication**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**|**.**<br>**.**|**. **|**v**|Machine Wallet is not downloaded<br>.<br>.<br>.|.|. 18|
|---|---|---|---|---|---|---|
|Intended audience<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.<br>.||. v|Operational issues .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.|. 19|
|Publications<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.<br>.||. v|Cannot sign up through AccessAgent or Web|||
|IBM Security Access Manager for Enterprise<br>Single Sign-On library .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>. v<br>Accessing terminology online .<br>.<br>.<br>.<br>.<br>.<br>. vii<br>Accessing publications online .<br>.<br>.<br>.<br>.<br>.<br>. vii<br>Ordering publications .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>. vii<br>Accessibility .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>. viii<br>Tivoli technical training .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>. viii<br>Tivoli user groups .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>. viii<br>Support information .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>. viii<br>Conventions used in this publication<br>.<br>.<br>.<br>.<br>. viii<br>Typeface conventions<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>. ix<br>Operating system-dependent variables and paths<br>ix||||Workplace .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>Cannot log on to AccessAdmin .<br>.<br>.<br>.<br>.<br>Form-based logon to AccessAdmin does not<br>work<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>Cannot connect to AccessAdmin<br>.<br>.<br>.<br>.<br>AccessAdmin - Service is not available<br>.<br>.<br>Cannot log on to the Integrated Solutions<br>Console.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>IBM HTTP Server does not start<br>.<br>.<br>.<br>.<br>Cannot open the httpd.conf file.<br>.<br>.<br>.<br>.<br>IMS Server configuration failed.<br>.<br>.<br>.<br>.<br>Directory server configuration issues .<br>.<br>.<br>Node federation failed.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|. 19<br>. 20<br>. 20<br>. 21<br>. 21<br>. 21<br>. 23<br>. 23<br>. 23<br>. 24<br>. 24|
|**Chapter 1. Troubleshooting and support**|||**1**|Cannot authenticate when a repository is down<br>IMS Server cannot issue a certificate for an||25|
|**Chapter 2. Learning more .**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**. **<br>About troubleshooting .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>About connectivity problems .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>About Security Access Manager for Enterprise Single<br>Sign-On .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>About fixes and updates<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>About messages .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>About performance problems and hangs .<br>.<br>.<br>.<br>About traps, crashes, and abends<br>.<br>.<br>.<br>.<br>.<br>.|||**3**<br>. 3<br>. 5<br>. 5<br>. 6<br>. 7<br>. 7<br>. 8|application<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>Policy pid_ts_logon_cache_enabled is not<br>displayed .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>AccessProfile is not displayed in the properties<br>pane.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>AccessStudio might crash when you use the<br>**Convert to** option<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>Cannot single sign-on in a command prompt .<br>OutOfMemory error when opening an<br>AccessProfile .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.||. 25<br>. 25<br>. 26<br>. 26<br>. 26<br>. 27|
|**Chapter 3. Troubleshooting checklist .**||**. **|**9**|Slow performance, startup and logon failure<br>Browser-related issues .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.<br>.|. 27<br>. 28|
|||||File download fails when using a Microsoft|||
|**Chapter 4. Known problems and**<br>**solutions .**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**|**.**<br>**. **||**11**|Internet Explorer browser.<br>.<br>.<br>.<br>.<br>.<br>.<br>Microsoft Internet Explorer crashes<br>.<br>.<br>.|.<br>.|. 28<br>. 28|
|Installation issues<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>Cannot install AccessAgent .<br>.<br>.<br>.<br>.<br>.<br>.<br>Cannot install the IMS Server<br>.<br>.<br>.<br>.<br>.<br>.<br>AccessAgent cannot connect to the IMS Server<br>AccessAgent cannot download the IMS Server<br>certificate .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>Conflict with another application .<br>.<br>.<br>.<br>.<br>AccessAgent cannot register the module.<br>.<br>.<br>Authentication factor issues .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>Cannot register an Active RFID card .<br>.<br>.<br>.||. <br>. <br>. <br>. <br>. <br>. <br>. <br>. <br>.|11<br> 11<br> 12<br> 13<br> 13<br> 13<br> 14<br> 14<br> 14|Mozilla Firefox interferes with the AccessAgent<br>single sign-on feature .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>Single sign-on does not work in Mozilla Firefox<br>Cannot capture logon credentials in Mozilla<br>Firefox pop-up window<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>Cannot launch web applications<br>.<br>.<br>.<br>.<br>.<br>Back button does not work .<br>.<br>.<br>.<br>.<br>.<br>.<br>Verifications .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>Determining the type of IMS Server deployment<br>Determining the Server AccessAgent mode .<br>.||. 29<br>29<br>. 30<br>. 30<br>. 30<br>. 30<br>31<br>. 31|
|Cannot unlock computer with the Active RFID<br>card .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.||.|15|**Chapter 5. Fixes.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**|**. **|**33**|
|Cannot log on to Wallet using Active RFID <br>Lost authentication devices .<br>.<br>.<br>.<br>.|card<br>.<br>.|.|15<br> 16|Obtaining fixes .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>Receiving fix notifications<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.<br>.|. 33<br>. 33|
|Bio-key verification UI is not displayed on|the||||||
|private desktop .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.<br>.|.|16|**Chapter 6. Searching knowledge bases**||**35**|
|Password issues .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.<br>.|.|16||||
|Common password issues<br>.<br>.<br>.<br>.<br>.<br>Cannot log on to AccessAssistant or Web|.<br>.|.|17|**Chapter 7. Analyzing data**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**|**. **|**37**|
|Workplace - password is not synchronized <br>Wallet-related issues<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.<br>.<br>.<br>.|. <br>.|17<br> 17|**Chapter 8. Collecting data**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**|**. **|**39**|
|Common Wallet issues<br>.<br>.<br>.<br>.<br>.<br>.|.<br>.|.|18|Message and trace logs<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.|. 39|
|||||Message logs .<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.|. 40|
|© Copyright IBM Corp. 2002 2012||||||**iii**|

|**About this publicati**|**on**|**.**|**.**|**.**|**.**|**.**||**.**|**.**|**.**|**. v**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Intended audience<br>.<br>.|.|.|.|.|.||.|.|.|.|. v|
|Publications<br>.<br>.<br>.<br>.|.|.|.|.|.|.||.|.|.|. v|
|IBM Security Access Manager||||for|Enterprise|||||||
|Single Sign-On library|.|.|.|.|.||.|.|.|.|. v|
|Accessing terminology|online|||.|.|.||.|.|.|. vii|
|Accessing publications|online|||.|.|.||.|.|.|. vii|
|Ordering publications .|.|.||.|.|.||.|.|.|. vii|
|Accessibility .<br>.<br>.<br>.<br>.|.|.||.|.|.|.|.|.|.|viii|
|Tivoli technical training .|.|.||.|.|.|.|.|.|.|viii|
|Tivoli user groups .<br>.<br>.|.|.||.|.|.|.|.|.|.|viii|
|Support information .<br>.|.|.||.|.|.|.|.|.|.|viii|
|Conventions used in this publication||||||.|.|.|.|.|viii|
|Typeface conventions|.|.|.|.|.|.||.|.|.|. ix|
|Operating system-dependent|||variables||||and||paths<br>ix|||

© Copyright IBM Corp. 2002, 2012 

|Trace logs .<br>.<br>.<br>.<br>.<br>.|.|.|.|.|.|.|.|. 41|IBM Support Assistant.|IBM Support Assistant.|.||.|.|.|.||.||.||.||.|. 49|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Configuring log settings .<br>.|.|.|.|.|.|.|.|. 42|IBM software maintenance|||contracts||||.||.||.||.||.|. 50|
|Configuring message logging||.|.|.|.|.|.|. 42|Determining the business||impact||||.|.||.||.||.||.|. 51|
|Enabling trace logging.<br>.|.|.|.|.|.|.|.|. 43|Describing a problem|.|.||.|.|.|.||.||.||.||.|. 51|
|Viewing logs .<br>.<br>.<br>.<br>.<br>.|.|.|.|.|.|.|.|. 45|Submitting data .<br>.|.|.||.|.|.|.||.||.||.||.|. 51|
|Using IBM Support Assistant|.|.|.|.|.|.|.|. 45||||||||||||||||||
|Using the IBM Support Assistant|||in|graphical|||||**Notices**<br>**.**<br>**.**<br>**.**<br>**.**|**.**||**.**|**.**|**.**|**.**||**.**||**.**||**.**||**.**||**. 55**|
|mode<br>.<br>.<br>.<br>.<br>.<br>.<br>.|.|.|.|.|.|.|.|. 45||||||||||||||||||
|Using the IBM Support Assistant <br>mode<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.|||in <br>.|console<br>.<br>.<br>.|||.|. 46|**Glossary .**<br>**.**<br>**.**<br>**.**|**.**||**.**|**.**|**.**|**.**||**.**||**.**||**.**||**.**||**. 59**|
|**Chapter 9. Contacting **|**support**|||**.**|**.**|**.**||**. 49**|**Index**<br>**.**<br>**.**<br>**.**<br>**.**<br>**.**|**.**||**.**|**.**|**.**|**.**||**.**||**.**||**.**||**.**||**. 67**|

**iv** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **About this publication** 

IBM[®] Security Access Manager for Enterprise Single Sign-On provides sign-on and sign-off automation, authentication management, and user tracking to provide a seamless path to strong digital identity. The _IBM Security Access Manager for Enterprise Single Sign-On Troubleshooting and Support Guide_ provides information about troubleshooting the different components of the product. 

## **Intended audience** 

This publication is for new and experienced users of IBM Security Access Manager for Enterprise Single Sign-On AccessAgent, AccessAssistant, and Web Workplace. 

This publication is for users who need to perform the following tasks: 

- v Usage workflow setup (for personal workstations, shared desktops, private desktops, and roaming desktops) 

- v Password and authentication setup 

- v Remote access setup for users 

- v Self-service tasks, such as resetting passwords, logging on using AccessAssistant, and unlocking Active Directory accounts 

Readers need to be familiar with the following topics: 

- v Installing and setting up authentication factors 

- v The workflow preferences of the organization (for example, for tasks such as sign-up, logon, logoff, and unlock workstations) 

## **Publications** 

This section lists publications in the IBM Security Access Manager for Enterprise Single Sign-On library. The section also describes how to access Tivoli[®] publications online and how to order Tivoli publications. 

## **IBM Security Access Manager for Enterprise Single Sign-On library** 

The following documents are available in the IBM Security Access Manager for Enterprise Single Sign-On library: 

- v _IBM Security Access Manager for Enterprise Single Sign-On Quick Start Guide_ , CF38DML 

Read this guide for a quick start on the main installation and configuration tasks to deploy and use IBM Security Access Manager for Enterprise Single Sign-On. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Planning and Deployment Guide_ , SC23995203 

Read this guide before you do any installation or configuration tasks. This guide helps you to plan your deployment and prepare your environment. It provides an overview of the product features and components, the required installation and configuration, and the different deployment scenarios. It also describes how to achieve high availability and disaster recovery. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Installation Guide_ , GI11930901 

© Copyright IBM Corp. 2002, 2012 

**v** 

Read this guide for the detailed procedures on installation, upgrade, or uninstallation of IBM Security Access Manager for Enterprise Single Sign-On. 

This guide helps you to install the different product components and their required middleware, and also do the initial configurations required to complete the product deployment. It covers procedures for using virtual appliance, WebSphere[®] Application Server Base editions, and Network Deployment. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Configuration Guide_ , GC23969201 

Read this guide if you want to configure the IMS Server settings, the AccessAgent user interface, and its behavior. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Administrator Guide_ , SC23995103 

This guide is intended for the Administrators. It covers the different Administrator tasks. This guide provides procedures for creating and assigning policy templates, editing policy values, generating logs and reports, and backing up the IMS Server and its database. Use this guide together with the IBM Security Access Manager for Enterprise Single Sign-On Policies Definition Guide. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Help Desk Guide_ , SC23995303 

This guide is intended for Help desk officers. The guide helps Help desk officers to manage queries and requests from users usually about their authentication factors. Use this guide together with the IBM Security Access Manager for Enterprise Single Sign-On Policies Definition Guide. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Policies Definition Guide_ , SC23969401 

Read this guide for the detailed descriptions of the different user, machine, and system policies that Administrators can configure in AccessAdmin. Use this guide along with the IBM Security Access Manager for Enterprise Single Sign-On Administrator Guide. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Troubleshooting and Support Guide_ , GC23969301 

Read this guide if you have any issues with regards to installation, upgrade, and product usage. This guide covers the known issues and limitations of the product. It helps you determine the symptoms and workaround for the problem. It also provides information about fixes, knowledge bases, and support. 

- v _IBM Security Access Manager for Enterprise Single Sign-On AccessStudio Guide_ , SC23995603 

Read this guide if you want to create or edit profiles. This guide provides procedures for creating and editing standard and advanced AccessProfiles for different application types. It also covers information about managing authentication services and application objects, and information about other functions and features of AccessStudio. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Provisioning Integration Guide_ , SC23995703 

   - Read this guide for information about the different Java[™] and SOAP API for provisioning. It also covers procedures for installing and configuring the Provisioning Agent. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Web API for Credential Management Guide_ , SC14764600 

Read this guide if you want to install and configure the Web API for credential management. 

**vi** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

- v _IBM Security Access Manager for Enterprise Single Sign-On Lightweight AccessAgent mode on Terminal Server SDK Guide_ , SC14765700 

   - Read this guide for the details on how to develop a virtual channel connector that integrates AccessAgent with Terminal Services applications. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Serial ID SPI Guide_ , SC14762600 

   - IBM Security Access Manager for Enterprise Single Sign-On has a Service Provider Interface (SPI) for devices that contain serial numbers, such as RFID. See this guide to know how to integrate any device with serial numbers and use it as a second authentication factor with AccessAgent. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Context Management Integration Guide_ , SC23995403 

   - Read this guide if you want to install and configure the Context Management solution. 

- v _IBM Security Access Manager for Enterprise Single Sign-On User Guide_ , SC23995003 

   - This guide is intended for the end users. This guide provides instructions for using AccessAgent and Web Workplace. 

- v _IBM Security Access Manager for Enterprise Single Sign-On Error Message Reference Guide_ , GC14762400 

This guide describes all the informational, warning, and error messages associated with IBM Security Access Manager for Enterprise Single Sign-On. 

## **Accessing terminology online** 

The IBM Terminology Web site consolidates the terminology from IBM product libraries in one convenient location. You can access the Terminology Web site at the following Web address: 

http://www.ibm.com/software/globalization/terminology 

## **Accessing publications online** 

IBM posts publications for this and all other Tivoli products, as they become available and whenever they are updated, to the Tivoli Information Center Web site at http://www.ibm.com/tivoli/documentation. 

**Note:** If you print PDF documents on other than letter-sized paper, set the option in the **File** > **Print** window that allows Adobe Reader to print letter-sized pages on your local paper. 

## **Ordering publications** 

You can order many Tivoli publications online at http:// www.elink.ibmlink.ibm.com/publications/servlet/pbi.wss. 

You can also order by telephone by calling one of these numbers: 

- v In the United States: 800-879-2755 

- v In Canada: 800-426-4968 

In other countries, contact your software account representative to order Tivoli publications. To locate the telephone number of your local representative, perform the following steps: 

1. Go to http://www.elink.ibmlink.ibm.com/publications/servlet/pbi.wss. 

2. Select your country from the list and click **Go** . 

About this publication **vii** 

3. Click **About this site** in the main panel to see an information page that includes the telephone number of your local representative. 

## **Accessibility** 

Accessibility features help users with a physical disability, such as restricted mobility or limited vision, to use software products successfully. With this product, you can use assistive technologies to hear and navigate the interface. You can also use the keyboard instead of the mouse to operate all features of the graphical user interface. 

For additional information, see "Accessibility features" in the _IBM Security Access Manager for Enterprise Single Sign-On Planning and Deployment Guide_ . 

## **Tivoli technical training** 

For Tivoli technical training information, see the following IBM Tivoli Education Web site at http://www.ibm.com/software/tivoli/education. 

## **Tivoli user groups** 

Tivoli user groups are independent, user-run membership organizations that provide Tivoli users with information to assist them in the implementation of Tivoli Software solutions. Through these groups, members can share information and learn from the knowledge and experience of other Tivoli users. Tivoli user groups include the following members and groups: 

v 23,000+ members 

- v 144+ groups 

Access the link for the Tivoli Users Group at www.tivoli-ug.org. 

## **Support information** 

If you have a problem with your IBM software, you want to resolve it quickly. IBM provides the following ways for you to obtain the support you need: 

## **Online** 

Go to the IBM Software Support site at http://www.ibm.com/software/ support/probsub.html and follow the instructions. 

## **IBM Support Assistant** 

The IBM Support Assistant is a free local software serviceability workbench that helps you resolve questions and problems with IBM software products. The IBM Support Assistant provides quick access to support-related information and serviceability tools for problem determination. To install the IBM Support Assistant software, go to http://www.ibm.com/software/support/isa. 

## **Troubleshooting Guide** 

For more information about resolving problems, see the _IBM Security Access Manager for Enterprise Single Sign-On Troubleshooting and Support Guide_ . 

## **Conventions used in this publication** 

This publication uses several conventions for special terms and actions, operating system-dependent commands and paths, and margin graphics. 

**viii** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Typeface conventions** 

This publication uses the following typeface conventions: 

## **Bold** 

- v Lowercase commands and mixed case commands that are otherwise difficult to distinguish from surrounding text 

- v Interface controls (check boxes, push buttons, radio buttons, spin buttons, fields, folders, icons, list boxes, items inside list boxes, multicolumn lists, containers, menu choices, menu names, tabs, property sheets) and labels (such as **Tip:** and **Operating system considerations** :) 

- v Keywords and parameters in text 

## _Italic_ 

- v Citations (examples: titles of publications, diskettes, and CDs) 

- v Words defined in text (example: a nonswitched line is called a _point-to-point line_ ) 

- v Emphasis of words and letters (words as words example: "Use the word _that_ to introduce a restrictive clause."; letters as letters example: "The LUN address must start with the letter _L_ .") 

- v New terms in text (except in a definition list): a _view_ is a frame in a workspace that contains data. 

- v Variables and values you must provide: ... where _myname_ represents.... 

## **Monospace** 

- v Examples and code examples 

- v File names, programming keywords, and other elements that are difficult to distinguish from surrounding text 

- v Message text and prompts addressed to the user 

- v Text that the user must type 

- v Values for arguments or command options 

## **Operating system-dependent variables and paths** 

This publication uses the UNIX convention for specifying environment variables and for directory notation. 

When using the Windows command line, replace **$** _variable_ with **%** _variable_ **%** for environment variables and replace each forward slash ( **/** ) with a backslash ( **\** ) in directory paths. The names of environment variables are not always the same in the Windows and UNIX environments. For example, %TEMP% in Windows environments is equivalent to $TMPDIR in UNIX environments. 

**Note:** You can use the UNIX conventions if you are using the bash shell on a Windows system. 

About this publication **ix** 

**x** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Chapter 1. Troubleshooting and support** 

The troubleshooting process, in general, requires that you isolate and identify a problem, then seek a resolution. For IBM Security Access Manager for Enterprise Single Sign-On, you can use a troubleshooting checklist to help you. If the checklist does not lead you to a resolution, you can collect additional diagnostic data and analyze it yourself. You can also submit the data to IBM Software Support for analysis. 

Troubleshooting topics for IBM Security Access Manager for Enterprise Single Sign-On are organized according to the sequence of these steps: 

1. Learn more about a symptom or feature. 

Before you can successfully troubleshoot a symptom, or a problem with a specific product feature, you need a basic understanding of that symptom or feature. 

2. Follow the troubleshooting checklist for the appropriate feature or symptom. The troubleshooting checklist offers a series of questions to guide you through the process of isolating and identifying a problem. If the problem is known to IBM, the checklist guides you to a published fix, solution, or workaround. 

If the troubleshooting checklist has not led you to a resolution, continue to the next step. 

3. Collect diagnostic data. 

This information explains how to gather the necessary information that you, or IBM Software Support, must have to determine the source of a problem. 

4. Analyze diagnostic data. 

This information explains how to analyze the diagnostic data that you collected. 

**1** 

© Copyright IBM Corp. 2002, 2012 

**2** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **more Chapter 2. Learning** 

The first step in the troubleshooting process is to learn more about the problem symptoms, or about the affected product feature. 

The following topics can help you to acquire the conceptual information that you must effectively troubleshoot problems with IBM Security Access Manager for Enterprise Single Sign-On: 

- v “About troubleshooting” 

- v “About connectivity problems” on page 5 

- v “About Security Access Manager for Enterprise Single Sign-On” on page 5 

- v “About fixes and updates” on page 6 

- v “About messages” on page 7 

- v “About performance problems and hangs” on page 7 

- v “About traps, crashes, and abends” on page 8 

## **About troubleshooting** 

Troubleshooting is a systematic approach to solving a problem. The goal is to determine why something does not work as expected and how to resolve the problem. 

The first step in the troubleshooting process is to describe the problem completely. A problem description helps IBM to determine where to start in finding the cause of the problem. This step includes asking yourself basic questions, such as: 

- v What are the symptoms of the problem? 

- v Where does the problem occur? 

- v When does the problem occur? 

- v Under which conditions does the problem occur? 

- v Can the problem be reproduced? 

The answers to these questions typically lead to a good description of the problem. A good problem description is the best way to start down the path of problem resolution. 

## **What are the symptoms of the problem?** 

When starting to describe a problem, the most obvious question is "What is the problem?" The question might seem straightforward, however, you can break it down into several more-focused questions that create a more descriptive picture of the problem. These questions can include: 

- v Who, or what, is reporting the problem? 

- v What are the error codes and messages? 

- v How does the system fail? For example, is it a loop, hang, fail, performance degradation, or incorrect result? 

- v How does the problem affect the business? 

**3** 

© Copyright IBM Corp. 2002, 2012 

## **Where does the problem occur?** 

Determining where the problem originates is not always easy, but it is one of the most important steps in resolving a problem. Many layers of technology can exist between the reporting and failing components. Networks, disks, and drivers are only a few components to be considered when you are investigating problems. The following questions can help you to focus on where the problem occurs to isolate the problem layer. 

- v Is the problem specific to one platform or operating system, or is it common across multiple platforms or operating systems? 

- v Is the current environment and configuration supported? 

Remember that getting a report from one layer does not mean that the problem originated from that layer. Part of identifying where a problem originates is understanding the environment in which it exists. Take some time to completely describe the problem environment, including the operating system, its version, all corresponding software and versions, and hardware information. Confirm that you are running within an environment that is a supported configuration. Many problems can be traced back to incompatible levels of software that are not intended to run together or have not been fully tested together. 

## **When does the problem occur?** 

Develop a detailed timeline of events leading up to a failure, especially for those cases that are one-time occurrences. You can most easily trace the problem timeline by working backward: Start at the time an error was reported (as precisely as possible, even down to the millisecond), and work backward through the available logs and information. 

Typically, you must look only as far as the first suspicious event that you find in a diagnostic log. However, doing so is not always easy to do and takes practice. Knowing when to stop looking is especially difficult when multiple layers of technology are involved, and when each has its own diagnostic information. 

To develop a detailed timeline of events, try to answer these questions: 

- v Does the problem happen only at a certain time of day or night? 

- v How often does the problem happen? 

- v What sequence of events leads up to the time that the problem is reported? 

- v Does the problem happen after an environment change, such as upgrading or installing software or hardware? 

Responding to the preceding questions can help to provide you with a frame of reference in which to investigate the problem. 

## **Under which conditions does the problem occur?** 

Knowing what other systems and applications are running at the time that a problem occurs is an important part of troubleshooting. These and other questions about your environment can help you to identify the root cause of the problem: 

- v Does the problem always occur when the same task is being performed? 

- v Does a certain sequence of events must occur for the problem to surface? 

- v Do any other applications fail at the same time? 

**4** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Can the problem be reproduced?** 

From a troubleshooting standpoint, the ideal problem is one that can be reproduced. Typically with problems that can be reproduced, you have a larger set of tools or procedures at your disposal to help you investigate. Consequently, problems that you can reproduce are often easier to debug and solve. However, problems that you can reproduce can have a disadvantage. If the problem significantly affects business, you do not want it to recur. If possible, recreate the problem in a test or development environment, which typically offers you more flexibility and control during your investigation. 

- v Can the problem be recreated on a test machine? 

- v Are multiple users or applications encountering the same type of problem? 

- v Can the problem be recreated by running a single command, a set of commands, or a particular application, or a stand-alone application? 

## **About connectivity problems** 

Connectivity problems typically involve multiple systems, including software, hardware, and communications. The best way to troubleshoot connectivity problems is through a process of elimination. 

First, collect relevant data and determine what you know, what data you have not yet collected, and what paths you can eliminate. At a minimum, answer the following questions. 

- v Are the communication paths operational? 

- v Has the initial connection been successful? 

- v Is the problem intermittent or persistent? 

- v Have changes been made to the communication network that would invalidate the previous directory entries? 

- v Where is the communication breakdown encountered? For example, was the breakdown between the client and a server? 

- v Is the problem encountered only within a specific application? 

- v What can you determine by the content of the message and the tokens that are returned in the message? 

- v Are other systems able to perform similar tasks successfully? If the task is a remote task, is it successful when performed locally? 

Next, try to isolate the problem by answering the questions in the Chapter 3, “Troubleshooting checklist,” on page 9. 

## **About Security Access Manager for Enterprise Single Sign-On** 

The first step to troubleshooting a problem is to learn about the affected feature of the software. 

You can learn more about IBM Security Access Manager for Single Sign-On from the information center: http://publib.boulder.ibm.com/infocenter/tivihelp/v2r1/ topic/com.ibm.itamesso.doc/ic-homepage.html. 

Chapter 2. Learning more **5** 

## **About fixes and updates** 

If you encounter a problem with the IBM Security Access Manager for Enterprise Single Sign-On software, first check the list of updates to confirm that your software is at the latest maintenance level. Next, check the list of problems fixed to see if IBM has already published an individual fix to resolve your problem. 

These lists are located at the Tivoli Support Web site for IBM Security Access Manager for Enterprise Single Sign-On http://www.ibm.com/software/sysmgmt/ products/support/index.html. Select **IBM Security Access Manager for Enterprise Single Sign-On** from the **Support for specific Tivoli products** list. 

Individual fixes are published as often as necessary to resolve defects in IBM Security Access Manager for Enterprise Single Sign-On. Two kinds of cumulative collections of fixes, called fix packs and refresh packs, are published periodically for IBM Security Access Manager for Enterprise Single Sign-On. Fix packs and refresh packs bring users up to the latest maintenance level. Install these update packages as early as possible to prevent problems. 

To receive weekly notification of fixes and updates, subscribe to My Support email updates. For more information, refer to “Receiving fix notifications” on page 33. 

The following table describes the characteristics of each fix. 

_Table 1. Maintenance types_ 

|||**Name**|**Characteristics**|||||
|---|---|---|---|---|---|---|---|
|||Fix|v A single fix that is published between updates to resolve a specific|||||
||||problem.|||||
||||v After you install a fix, test any functions|||that the fixed component might||
||||affect.|||||
|||Fix pack|v A fix pack contains all fixes that have been published since the previous fix|||||
||||pack or refresh pack. A fix pack might also contain new fixes.|||||
||||v Fix packs increment the modification level of the product and are named|||||
||||accordingly, for example, 5.0.1|||||
||||v A fix pack can update specific components, or it can update the entire|||||
||||product image.|||||
||||v During fix pack installation, all previously applied fixes are automatically|||||
||||uninstalled.|||||
||||v After you install a fix pack, conduct a regression-test for all of the critical|||||
||||functions.|||||
||||v The most recent two fix packs are available for download (for example,|||||
||||5.0.2 and 5.0.1). Earlier fix packs||are not|available.||
|||Refresh<br>pack|v A refresh pack contains all fixes that have been published since the<br>previous fix pack or refresh pack, and new fixes.|||||
||||v A refresh pack typically contains||new function, in addition to fixes, and it|||
||||updates the entire product image.|||||
||||v Refresh packs increment the modification level of the product and are|||||
||||named accordingly, for example,||5.0.1.|||
||||v During refresh pack installation,||all previously applied fixes are|||
||||automatically uninstalled.|||||
||||v After you install a refresh pack, you conduct a regression-test on all of the|||||
||||critical functions.|||||

**6** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **About messages** 

You can often resolve the problem stated in the warning or error message you get from IBM Security Access Manager for Enterprise Single Sign-On by reading the entire message text and the recovery actions that are associated with the message. 

You can find the full text of messages, their explanations, and the recovery actions by searching for the message identifier in the IBM Security Access Manager for Enterprise Single Sign-On Error Message Reference Guide. 

## **About performance problems and hangs** 

Performance problems arise in many different situations. A hang is one type of performance problem in which users wait for a response for an indefinite time. Troubleshooting techniques for hangs are similar to the techniques you would use for other performance problems. 

Here are some examples of situations in which performance problems become evident: 

- v Query performance is slower than expected. 

- v The workload or a batch job is not completing as soon as expected, or a reduction in the transaction rate or throughput occurs. 

- v The overall system slows down. 

- v A bottleneck is suspected in one of the system resources such as processor, I/O, or memory. 

- v Query or other workload processing is using more resource than is expected or available. 

- v One system is performing better than another. 

- v A query, application, or system hangs. 

Hangs can be difficult to troubleshoot because the symptoms often seem to match the symptoms of other problems. For example, if a user is waiting for a long time for a response from a query, that user might think that the system hanged. In many cases, the query might be complex, and the system might also be heavily used at the time, so the system has not hung. But, the system might be slow to respond. Also, during a system shutdown, a significant buildup of activity can result in most or all commands seem to hang. 

Aside from characterizing the problem correctly in terms of what the symptoms are, and where the symptoms are observed, you need several other pieces of information to put the problem in context. Symptoms typically range from slowness, too much resource used, and so on. The symptoms are typically found in a query, application, system resource, and so on. 

Answer the following questions to quickly determine the best place to start looking for the cause of the performance problem. 

1. When did the problem first occur? 

   - If the problem has been occurring for some time, you might be able to use historical data to find differences. Historical data helps you to focus on changes in system behavior and then focus on why these changes were introduced. You also must consider whether any recent changes occurred, such as hardware or software upgrades, a new application rollout, additional users, and so on. 

2. Is the performance issue constant or intermittent? 

Chapter 2. Learning more **7** 

If the poor performance is continual, check if the system has started to handle a larger workload. You can also check if a shared database resource has become a bottleneck. Other potential causes of performance degradation include increased user activity, multiple large applications, or removal of hardware devices. If performance is poor only for brief periods, begin by looking for common applications or utilities that run at these times. If users report that a group of applications are experiencing performance issues, you can begin your analysis by focusing on these applications. 

3. Does the problem appear to be system-wide or isolated to IBM Security Access Manager for Enterprise Single Sign-On or its components? 

System-wide performance problems suggest an issue outside of IBM Security Access Manager for Enterprise Single Sign-On. Something at the operating system level must be addressed. 

4. If the problem is isolated to one component, does one particular activity cause the problem? 

If one component seems to be causing the problem, you can evaluate whether users who are reporting that specific activity, are experiencing a slowdown. You might be able to isolate the issue to one component and a specific activity. 

5. Do you notice any common characteristics of the poor performance, or does the problem occur in random? 

Determine if any common functions are involved. The function involvement might indicate that these functions are a point of contention. 

## **About traps, crashes, and abends** 

The terms _trap_ , _crash_ , and abnormally end ( _abend_ ) are often used synonymously. 

If IBM Security Access Manager for Enterprise Single Sign-On cannot continue processing as the result of a trap, segmentation violation, or exception, it generates an error. 

Most traps, crashes, and abends for IBM Security Access Manager for Enterprise Single Sign-On result in an exception. The exception is included in the message log, and typically does not require a trace to be enabled in order for it to be reported. However, these errors can be recorded in a trace log, if you are instructed to enable trace logging by IBM Support personnel. If you open a problem report with IBM, you must provide the trace log for analysis. 

These errors can be recorded in a trace log, if you are instructed to enable trace logging by IBM Support personnel. 

If you open a problem report with IBM, you might need to provide the trace log for analysis. 

Generate trace files only when IBM Software Support asks you to do so, although IBM Security Access Manager for Enterprise Single Sign-On can generate trace logs on demand. See “Trace logs” on page 41 for more information. 

**8** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Chapter 3. Troubleshooting checklist** 

The following questions can help you to identify the source of a problem that is occurring with IBM Security Access Manager for Enterprise Single Sign-On. 

1. Are your fixes and fix packs up to date? 

   - See “Obtaining fixes” on page 33 for more information. 

2. Does the IBM Knowledge Base contain additional information about the problem? 

   - See Chapter 6, “Searching knowledge bases,” on page 35. 

3. Are you receiving any error messages? 

   - See the IBM Security Access Manager for Enterprise Single Sign-On _IBM Security Access Manager for Enterprise Single Sign-On Error Message Reference_ for information about error messages. 

4. Do the logs contain any messages about the problem? 

   - See “Message logs” on page 40 and “Trace logs” on page 41 for more information. 

5. Does the problem occur while installing or uninstalling one of the following features? 

   - v IBM Security Access Manager for Enterprise Single Sign-On or its components 

      - See the _IBM Security Access Manager for Enterprise Single Sign-On Installation Guide_ . 

   - v WebSphere Application Server 

      - See the installation troubleshooting topics in the IBM WebSphere Application Server information center at http://www.ibm.com/software/webservers/ appserv/was/library/ 

6. Does the problem occur when you are configuring IBM Security Access Manager for Enterprise Single Sign-On? 

   - See the _IBM Security Access Manager for Enterprise Single Sign-On Configuration Guide_ . 

7. If you cannot resolve the problem in the preceding steps, gather additional information about the location of the problem, or conditions during which the problem occurs: 

   - v Did the problem occur during runtime processing? 

      - Did it fail to connect? 

      - Did it crash? 

      - Did it have a performance problem such as slow response, or a "hang"? 

      - Did it abend, trap, or throw a Java exception? 

   - v Does the problem occur while you configure a specific function? 

   - v Does the problem occur when you perform a specific task? 

The answers to these questions might help you determine the location of the problem and assist you in locating additional information about the problem. For example, if the problem occurs while configuring a specific function or performing a specific task, you might find a solution in the documentation of that function or task. 

**9** 

© Copyright IBM Corp. 2002, 2012 

If the checklist does not guide you to a resolution, you can collect additional diagnostic data. The additional data might be necessary to IBM Support personnel to help you continue troubleshooting the problem. See Chapter 8, “Collecting data,” on page 39. 

**10** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Chapter 4. Known problems and solutions** 

You might encounter some issues when deploying or using IBM Security Access Manager for Enterprise Single Sign-On. Select the possible category of the issue you encountered and search for the issue and workaround. 

See the following topics: 

- v “Installation issues” 

- v “Authentication factor issues” on page 14 

- v “Password issues” on page 16 

- v “Wallet-related issues” on page 17 

- v “Operational issues” on page 19 

- v “Browser-related issues” on page 28 

- v “Verifications” on page 30 

To get more information about the issue, see Chapter 8, “Collecting data,” on page 39. 

## **Installation issues** 

You can encounter issues during or after installing the product component. These issues can prevent you from successfully installing or using the component. 

See the following topics for the possible issues and workaround. 

- v “Cannot install AccessAgent” 

- v “Cannot install the IMS[™] Server” on page 12 

- v “AccessAgent cannot connect to the IMS Server” on page 13 

- v “AccessAgent cannot download the IMS Server certificate” on page 13 

- v “Conflict with another application” on page 13 

- v “AccessAgent cannot register the module” on page 14 

## **Cannot install AccessAgent** 

Different factors can cause the AccessAgent installation to fail. 

The AccessAgent installation can fail for any of the following reasons: 

**The AccessAgent installer might be corrupted.** 

The AccessAgent installation file might be corrupted if it is not downloaded properly. Download the file again and ensure that all the required files are available. 

**The AccessAgent is installed from a shared location or a server.** 

Do not install the AccessAgent from a shared location or server. Copy the installer to a local disk drive on your computer before you run the installer. 

**The AcessAgent installer is not compatible with the operating system.** 

If you are using a 64-bit operating system, use the 64-bit AccessAgent installer. If you are using a 32-bit operating system, use the 32-bit AccessAgent installer. 

**11** 

© Copyright IBM Corp. 2002, 2012 

**The user who installed AccessAgent does not have Administrator privileges.** To install AccessAgent, you must have Administrator privileges. 

## **You enabled the Windows settings Protect your data.** 

This setting prevents you to launch the AccessAgent installer. Right-click the installer, and clear the **Protect your data** option. 

## **Windows Scripting Host version is not enabled.** 

When you run the AccessAgent installer in silent mode, the installation is completed but when you restart the computer, the installation is corrupted. 

Check the following registries before you install AccessAgent: 

- v HKEY_CURRENT_USER\Software\Microsoft\Windows Script Host\Settings\Enabled 

- v HKEY_LOCAL_MACHINE\Software\Microsoft\Windows Script Host\Settings\Enabled 

## **Cannot install the IMS[™] Server** 

Different factors can cause the IMS Server installation to fail. 

The IMS Server installation can fail for any of the following reasons: 

## **Database server has low disk space** 

Before you install the IMS Server, ensure that you have enough disk space for the database server and for the computer hosting the IMS Server. See "Hardware and software requirements" in the _IBM Security Access Manager for Enterprise Single Sign-On Planning and Deployment Guide_ . 

## **WebSphere Application Server security details are not correct** 

Specify the correct application security details. 

- v Ensure that you enter the correct SOAP port. 

**Note:** You can determine the correct port number in the following directory for each profile. For example: 

Stand-alone : <was_home>/profiles/<AppSrv01>/logs/ AboutThisProfile.txt 

Network deployment: <was_home>/profiles/<Dmgr01>/logs/ AboutThisProfile.txt 

For example: 

   - For WebSphere Application Server stand-alone, the SOAP port for the application server is 8880. 

   - For WebSphere Application Server Network Deployment, the SOAP port for the Deployment Manager is 8879. 

- v If the security validation for WebSphere Application Server fails, you entered the wrong information. In this case, you can restart the installer. 

## **WebSphere Application Server administration security settings are not correct** 

Ensure that you specify the correct: 

- v WebSphere administrative user name and password 

- v SSL trusted keystore password 

## **WebSphere Application Server is not available** 

Ensure that: 

**12** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

- v The WebSphere Application Server is started. 

- v The host name can be resolved. 

## **AccessAgent cannot connect to the IMS Server** 

Different factors can affect the AccessAgent and IMS Server connection. 

To verify whether the computer can connect to the IMS Server, enter the AccessAdmin URL in your browser from the client computer. If the AccessAdmin page is not displayed, the connection is not established. 

AccessAgent cannot connect to the IMS Server for the following reasons: 

## **The IMS Server is not running.** 

Ensure that the ISAMESSOIMS application is started in the Integrated Solutions Console. 

## **The IMS Server location is not correct.** 

During installation, AccessAgent tries to automatically connect to the IMS Server. If a connection cannot be established, you are prompted to enter the location of the IMS Server. Ensure that the information provided is correct. 

## **IMS Server certificate "cn" is not consistent with AccessAgent** 

Ensure that the cn of the IMS Server certificate is the same name provided for the AccessAgent. 

## **There is no network connection.** 

Ensure that you have Internet connection. 

## **The client computer has a personal firewall or anti-spyware that blocks traffic from AccessAgent.** 

Ensure that the personal firewall or anti-spyware does not block traffic from winlogon.exe. 

## **AccessAgent cannot download the IMS Server certificate** 

The IMS Server certificate download might fail if AccessAgent cannot connect to the IMS Server. The IMS Server certificate is used to identify the IMS Server. 

This problem occurs when: 

- v AccessAgent tries to connect with the IMS Server but because of a heavy load, the connection times out. 

- v The IMS Server is starting up and the connection fails because the IMS Server is not yet available. 

If configured properly, AccessAgent downloads the IMS Server certificate to the computer. If the IMS Server certificate is not automatically downloaded, download it through the following options after you install AccessAgent: 

- v Select **Start** > **All Programs** > **AccessAgent** > **Set IMS Server Location** . 

- v Run C:\Program Files\IBM\ISAM ESSO\SetupCertDlg.exe. 

## **Conflict with another application** 

Certain applications installed on your computer can conflict with the AccessAgent installation. 

Chapter 4. Known problems and solutions **13** 

**Symptom:** During the AccessAgent installation, the following message is displayed: 

The AccessAgent setup has detected a conflict with <Application Name> which is installed on your computer. This conflict might not allow AccessAgent to run properly. Uninstall the conflicting application. Click Yes to exit from the setup. Click No to ignore the conflict and continue with the installation. 

## **Solution:** 

1. Cancel the AccessAgent installation. 

2. Uninstall the application that causes the conflict. 

**Note:** Make sure that the application is no longer used before you uninstall the application. 

3. Run the AccessAgent installer again. 

**Note:** AccessAgent might not work properly if you ignore the message prompt and continue with the installation. 

## **AccessAgent cannot register the module** 

You might encounter a module-related problem during the AccessAgent installation. 

**Symptom:** During the AccessAgent installation, the following message is displayed: 

The system encountered a problem while registering a module (Error 1904). 

## **Solution:** 

1. Ensure that: 

   - v You have Administrator privileges. 

   - v You have permissions to write into the registry. 

   - v No third-party applications prevent your access to the system32.dll registry. 

2. Uninstall AccessAgent. 

3. Install AccessAgent. 

## **Authentication factor issues** 

You can encounter issues when you register or use an authentication factor. 

See the following topics for the possible issues and workaround. 

- v “Cannot register an Active RFID card” 

- v “Cannot unlock computer with the Active RFID card” on page 15 

- v “Cannot log on to Wallet using Active RFID card” on page 15 

- v “Lost authentication devices” on page 16 

- v “Bio-key verification UI is not displayed on the private desktop” on page 16 

## **Cannot register an Active RFID card** 

Different factors can cause the Active RFID card registration to fail. 

The registration can fail for any of the following reasons: 

**14** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **The Active RFID card is already registered** 

A message is displayed if the Active RFID card is already registered to the IMS Server. The Active RFID card is used by another user, but is not revoked from the IMS Server. 

Return the Active RFID card and request for a new Active RFID card. 

## **The Active RFID card is revoked** 

The Active RFID card must be revoked when it is reported as lost. If the lost Active RFID card is found and it is used to log on to AccessAgent, a message is displayed that the Active RFID is revoked. 

To use a revoked Active RFID card, request for an authorization code. 

## **Cannot detect the Active RFID Card** 

The distance and placement of the card from the reader can affect the reception of the RFID signal. The reader and the card must be positioned at the same level. For example: If the reader is mounted on the monitor, the card must be placed on the upper part of the body. 

## **Cannot unlock computer with the Active RFID card** 

Restart the Active RFID card or use the **Go to Windows to unlock** option to unlock the computer if the Active RFID card does not work. 

**Symptom:** When you unlock the computer by using an Active RFID card, a message is displayed that the password cannot be validated. 

## **Solution:** 

1. Switch off the Active RFID card and then turn it on. 

2. Select the Active RFID card from the list. 

3. Enter the corresponding password. 

4. If the problem persists, use the Windows user name and password to unlock the computer. 

5. Select **Go to Windows to unlock** in the navigation panel of the Unlock This Computer window. 

6. Log on to Windows. 

7. Reset the Windows password. 

## **Cannot log on to Wallet using Active RFID card** 

You cannot log on to the Wallet when using an Active RFID card either because of the password you entered or because of the Active RFID card or reader. 

The Wallet logon can fail for the following reasons: 

## **Wrong password** 

You entered a wrong password. Enter the password again. 

**Note:** Ensure that the Caps Lock key is not active and that the password characters are entered in the correct case. 

## **Forgotten the password** 

If you forgot the password, request for an authorization code so that you can reset the password. 

## **Damaged or corrupted Active RFID card or reader** 

Chapter 4. Known problems and solutions **15** 

If the Active RFID is damaged or corrupted, request for a replacement. 

## **Unable to detect the Active RFID card** 

There might be: 

- v A timeout for detecting the Active RFID card. The card might be automatically turned off if it is switched on for more than nine hours. Switch off the card and turn it on. If the problem persists, restart the computer. 

- v A substantial reduction on battery power. In this case, replace the battery. 

## **Lost authentication devices** 

Smart cards, RFID cards or Active RFID cards are devices used to log on, to lock AccessAgent, to unlock AccessAgent, and to access the Wallet. If you lost your authentication device, you cannot log on to your Wallet and you cannot perform single sign-on to your applications. 

If you lost your authentication device: 

1. Request for a new smart card, RFID card or Active RFID card, whichever is applicable. 

2. Request for an authorization code. 

The authorization code is required to associate the Wallet with the new authentication device and to obtain temporary access to the Wallet in case the replacement is not yet available. 

## **Bio-key verification UI is not displayed on the private desktop** 

When you scan your fingerprint into the fingerprint reader and it is not successful, the BIO-key verification UI must be displayed. 

**Symptom:** The BIO-key verification UI is enabled. However, the verification UI is not displayed when your fingerprint scan failed because of bad quality. 

## **Solution:** 

1. Open the Registry Editor. 

2. Navigate to [HKEY_LOCAL_MACHINE\SOFTWARE\IBM\ISAM ESSO\SOCIAccess\ DSPList\{6EA4B6D4-8CDF-4C4E-8B40-CA6A20D0CD6B}\Devices\{5994DB8B-A2C34e0a-BC79-F274AE5ECC11}\UISPList\{68F86CB2-630B-4F15-9E2B-5A77B294E9E2}] 

3. Set the **Enabled** registry value to 1. 

4. Log off from Windows. 

5. Log on to Windows. 

**Note:** If you are using Windows XP, restart the computer for the changes to take effect in EnGINA. 

## **Password issues** 

You can encounter issues when you change or reset passwords, or when the ISAM ESSO password is not synchronized with the Active Directory password. 

See the following topics for the possible issues and workaround: 

- v “Common password issues” on page 17 

**16** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

- v “Cannot log on to AccessAssistant or Web Workplace - password is not synchronized” 

## **Common password issues** 

The ISAM ESSO password is used to authenticate the identity of the user. The user must be authenticated before the user can access the system. You might encounter issues when you log on with your password or when you change or reset your password. 

AccessAgent might not accept your password for any of the following reasons: 

## **You did not enter the correct password.** 

If you have forgotten the password, request for an authorization code from the Help desk to reset the password. 

## **You did not enter the password in the correct case.** 

Check if the Caps Lock key is active, and that the characters are entered in the correct case. 

**Your password is not within the required length.** 

Password length can be configured by the Administrator. The password length can range from 6 to 20 characters, depending on the preference of the organization. Enter a new password that complies with the password length policy. 

**You did not enter the same password in the Confirm password field.** 

When you change the password, enter the same password in both the new password field and confirm password field. 

## **Cannot log on to AccessAssistant or Web Workplace - password is not synchronized** 

If the ISAM ESSO password is not synchronized with the Active Directory password, your logon might fail. 

The issue occurs when: 

1. You change or reset your password on AccessAgent. 

2. You log on to AccessAssistant or Web Workplace with the old password. 

The following error message is displayed: ISAM ESSO password is not synchronized with Active Directory password. 

This behavior is caused by a Microsoft limitation. For more information, see http://support.microsoft.com/kb/906305/en-us 

## **Wallet-related issues** 

You can encounter issues when using, downloading, or logging on to the Wallet. 

See the following topics for the possible issues and workaround: 

- v “Common Wallet issues” on page 18 

- v “Machine Wallet is not downloaded” on page 18 

Chapter 4. Known problems and solutions **17** 

## **Common Wallet issues** 

You might encounter issues when using the machine or user Wallet. See this topic for the common Wallet issues and the possible solutions. 

## **Cannot use shared cached Wallet** 

A shared cached Wallet cannot be used if copy protection is enabled. Do not enable the policy for a shared Wallet deployment. 

For more information, see pid_wallet_cache_security_enabled in the _IBM Security Access Manager for Enterprise Single Sign-On Policies Definition Guide_ . 

## **Temporary access to Wallet is expired** 

If you are given temporary access to the Wallet, the access is only valid for a predefined time. When the validity of the temporary access expires, you can no longer use the Wallet. Request for a new authorization code so that you can access the Wallet. 

## **Wallet is locked** 

The Wallet is locked after a predefined number of failed logon attempts. The number of allowed failed logon attempts can be configured by the Administrator. 

If your Wallet is locked, contact the Administrator. 

## **Machine Wallet is not downloaded** 

AccessAgent creates the machine Wallet by downloading the latest policies and AccessProfiles from the current IMS Server. 

You cannot log on to AccessAgent if the policies and AccessProfiles from the IMS Server are not downloaded successfully. 

If AccessAgent cannot connect to the IMS Server, AccessAgent uses the policies and AccessProfiles specified in this file: C:\Program Files\ISAM ESSO\AA\all_sync_data.xml. 

If AccessAgent cannot successfully download the policies and AccessProfiles from the IMS Server after several manual synchronization attempts, see “Downloading the machine Wallet.” 

## **Verifying the downloaded machine Wallet** 

Complete this procedure to confirm that the machine Wallet was downloaded properly. 

1. Run AccessStudio. 

2. Load AccessProfiles from AccessAgent. 

3. Click **sso_site_web_ims_admin** under **AccessProfiles** . 

The machine Wallet is correct if the **@domain** field on the right panel is set to the **IMS Server name** . The machine Wallet is not downloaded properly if the **@domain** field displays **$hostname** . 

## **Downloading the machine Wallet** 

Download the machine Wallet again if the machine Wallet is corrupted. 

1. Log off from AccessAgent, if you are logged on. 

**18** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

2. Stop the following AccessAgent processes through the Task Manager. v AATray.exe 

   - v Sync.exe 

3. Stop the DataProvider service by using net stop dataprovider. 

4. Stop the SOCIAccess service by using net stop sociaccess. The SOCIAccess service automatically replaces any deleted machine Wallet file. 

5. Delete the machine Wallet (machine.wlt). 

6. Restart the computer. 

7. Launch AccessStudio. 

8. Select **Tools** > **Backup System Data from IMS to File** . 

9. Click **Backup** . 

10. Save all_sync_data.xml in the Config folder of the AccessAgent installer package. 

## **Operational issues** 

You can encounter issues when using the product components such as the IMS Server, AccessAgent, AccessStudio, AccessAdmin, AccessAssistant, or WebWorkplace. Issues can be related to performance, to the browser, to the machine Wallet, or to the user Wallet. 

See the following topics for the possible issues and solutions: 

- v “Cannot sign up through AccessAgent or Web Workplace” 

- v “Cannot log on to AccessAdmin” on page 20 

- v “Form-based logon to AccessAdmin does not work” on page 20 

- v “Cannot connect to AccessAdmin” on page 21 

- v “AccessAdmin - Service is not available” on page 21 

- v “Cannot log on to the Integrated Solutions Console” on page 21 

- v “IBM HTTP Server does not start” on page 23 

- v “Cannot open the httpd.conf file” on page 23 

- v “IMS Server configuration failed” on page 23 

- v “Directory server configuration issues” on page 24 

- v “Node federation failed” on page 24 

- v “Cannot authenticate when a repository is down” on page 25 

- v “IMS Server cannot issue a certificate for an application” on page 25 

- v “Policy pid_ts_logon_cache_enabled is not displayed” on page 25 

- v “AccessProfile is not displayed in the properties pane” on page 26 

- v “AccessStudio might crash when you use the **Convert to** option” on page 26 

- v “Cannot single sign-on in a command prompt” on page 26 

- v “OutOfMemory error when opening an AccessProfile” on page 27 

- v “Slow performance, startup and logon failure” on page 27 

## **Cannot sign up through AccessAgent or Web Workplace** 

The user cannot sign up with AccessAgent or Web Workplace if the user name that is stored in the Active Directory contains a special character, such as apostrophe (’). 

**Symptom:** This issue occurs for the following scenario: 

Chapter 4. Known problems and solutions **19** 

1. IMS Server is installed and configured properly with WebSphere Application Server 7 and fix pack 9. 

2. The directory server is configured properly. 

3. When the user signs up with AccessAgent or Web Workplace, the following error message is displayed: 

Unable to register due to an unexpected error. Try again. If the problem persists, contact your Helpdesk. 

**Solution:** Apply WebSphere Application Server fix pack 15 or later. 

## **Cannot log on to AccessAdmin** 

Different factors can cause the logon to AccessAdmin to fail. 

You cannot log on to AccessAdmin if: 

## **You do not have Administrator rights** 

You can log on to AccessAdmin only if you have Administrator or Help desk rights. 

## **The DNS name of the web server contains a special character.** 

Ensure that the DNS name does not contain special characters such as "_". 

## **Form-based logon is disabled** 

Ensure that form-based logon is enabled if: 

- v You are logging on to AccessAdmin from a browser on a remote computer, and 

- v You are not logged on to AccessAgent on that remote computer. 

- Form-based logon is not required if: 

- v You are logging on to AccessAdmin from a browser on a local computer, and 

- v You are logged on to AccessAgent on that remote computer. 

## **Machine Wallet is not downloaded** 

If you log on to AccessAdmin from a browser on a remote computer and you are logged on to AccessAgent, ensure that the machine Wallet is downloaded. 

## **Form-based logon to AccessAdmin does not work** 

If form-based logon is not enabled, you cannot log on to AccessAdmin from a remote computer with AccessAgent. 

## **About this task** 

Form-based logon is enabled by default in IBM Security Access Manager for Enterprise Single Sign-On version 8.2. 

If form-based logon is not enabled by default in the previous release, and you upgraded to version 8.2, form-based logon is not enabled. The previous setting is carried forward in 8.2. 

**20** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Procedure** 

1. Open the IMS Configuration Utility. 

2. Select **AccessAdmin** > **Login** . 

3. Select **true** from the **Allow form-based login to AccessAdmin from remote machine** list. 

4. Click **Update** . 

**Note:** If the form-based logon is not working from the local IMS Server machine, use the URL https://localhost/admin from the IMS Server machine instead of the DNS domain name. 

5. For WebSphere Application Server stand-alone deployment, restart the ISAMESSOIMS application. 

For WebSphere Application Server network deployment, do a full synchronization, and then restart the cluster. 

## **Cannot connect to AccessAdmin** 

Different factors can affect the connection to AccessAdmin. 

You cannot connect to AccessAdmin if: 

## **The IMS Server is not running.** 

Ensure that the ISAMESSOIMS application is started in the Integrated Solutions Console. 

## **There is no network connection.** 

Ensure that you have a network connection before you start AccessAdmin. 

## **Ports are not available** 

Ensure that the required ports are available. 

## **- AccessAdmin Service is not available** 

When you open AccessAdmin, the Service is not available, and an error is displayed. Check the logs for the details. 

This error occurs on a WebSphere Application Server Network Deployment. 

**Symptom:** In the SystemOut.log file, you see the java.io serializable error. You did not override the session management for the ISAMESSOIMS EAR file. 

**Solution:** Override session management. See "Overriding session management for the ISAMESSOIMS" in the _IBM Security Access Manager for Enterprise Single Sign-On Installation Guide_ . 

## **Cannot log on to the Integrated Solutions Console** 

Different factors can cause the logon to the Integrated Solutions Console to fail. 

You cannot log on to the Integrated Solutions Console for any of the following reasons: 

## **Password is not correct** 

Ensure that you enter the correct password. 

**WebSphere Application Server administrator user name is stored in the WebSphere Application Server and in the Active Directory** 

Chapter 4. Known problems and solutions **21** 

- v The administrative user name that you supply for the WebSphere administrator must not exist on the directory server. Delete the user name from the Active Directory. 

- v Avoid creating an administrative user with the same user name as the WebSphere administrator. For example, if the WebSphere administrator you provide is wasadmin, then the user wasadmin must not exist on the corporate enterprise directory. 

- v Avoid the use of _administrator_ as the WebSphere Application Server administrator. 

- v Choose a user name that is least likely to conflict with your existing enterprise directory users. 

## **An Active Directory is down or cannot be reached** 

Ensure that all the Active Directories are available and reachable. 

## **Related issue: New user signup fails** 

If the lookup user password in Active Directory and on the IMS Configuration Utility are different, a new user sign up task fails. 

## **Symptom:** 

1. You cannot log on to the Integrated Solutions Console. 

2. You try to sign up the user, but it fails. 

## **Solution:** 

## **Option 1** 

Change the lookup user password to the old password. 

## **Option 2** 

When you create the lookup user in the Enterprise Directory, do not change the password and configure the password setting to password never expires. 

## **Option 3** 

1. Stop all WebSphere Application Server Java related processes. 

2. Modify the security.xml in <was_home>/profiles. 

   - Find the first instance of "enabled" and set the parameter value to False. 

**Tip:** Back up the security.xml file before you modify it. 

3. Start the WebSphere Application Server. 

4. On the Active Directory, either create a new lookup user or reset the password of the existing lookup user. 

5. On the IMS Configuration Utility, edit the enterprise directory for which the lookup user password is changed. 

6. Stop the WebSphere Application Server. 

7. Start the WebSphere Application Server. 

8. On the Integrated Solutions Console, enable the Administrative Security. 

   - a. On the Integrated Solutions Console navigation pane, select **Security** > **Global security** . 

   - b. On the **Global security** page, select **Enable administrative security** . 

   - c. Click **Apply** . 

**22** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## d. Click **Save** in the **Messages** box at the top of the page. 

## **IBM HTTP Server does not start** 

There are instances where you have to start the IBM HTTP Server during the IMS Server installation and configuration. 

The IBM HTTP Server cannot start if: 

## **There is already an application listening to the same port.** 

Use a utility like netstat to check if a port is already in use. For example: **netstat -na -p tcp -o** . 

## **The Administrator password is changed** 

Check whether the Administrator password was changed. If the password was changed, change the password for the service in the Windows service definition panel. 

## **Cannot open the httpd.conf file** 

When enabling the SSL directive, the httpd.conf file cannot be opened. This issue occurs when the IBM HTTP Server is down or the nodes are not started. 

**Symptom:** An error message is displayed when you open the httpd.conf file and the text area is empty. 

## **Solution:** 

1. If the web server is created on a managed node, check whether the node agent for this node is available or started. 

2. If the web server is created on a unmanaged node, check the credentials. 

   - a. In the administrator console, click **Servers** > **Server Types** > **Web servers** . 

   - b. Click the _<Web_server_name>_ . For example: webserver1. 

   - c. In the **Additional Properties** section on the **Configuration** tab, click **Remote Web Server Management** . 

   - d. Enter the IBM HTTP Server administration server authentication user ID and password. For example: ihsadmin. 

   - e. Clear the **Use SSL** check box. 

   - f. Click **OK** . 

   - g. In the **Messages** box, click **Save** . 

3. Start the IBM HTTP Server. 

## **IMS Server configuration failed** 

If you manually create a database and you want to create the schema manually, log out from the SQL database server as SA and log on to SQL. Log on to SQL using the user name you specified when you created a database user name and schema name. Otherwise, the IMS Server configuration might fail because of a wrong database configuration. This procedure must be done before you run the IMS Configuration wizard. 

**Symptom:** In the IMS Configuration wizard, when you click **Save** , the error message "Failed to upload IMS Server Soft CA" is displayed. 

## **Solution:** 

Chapter 4. Known problems and solutions **23** 

Check your schema name in the SQL database server if it belongs to the user that you created for the database. 

See the _IBM Security Access Manager for Enterprise Single Sign-On Installation Guide_ for the steps to set up the database and schema manually. 

To run the IMS Server configuration again, follow this procedure: 

- v Run the cleanImsConfig.bat script located in C:\Program Files\IBM\ISAM ESSO\IMS Server\bin\. 

- v Run the IMS configuration Wizard after setting up the database and schema. 

## **Directory server configuration issues** 

You might encounter issues related to the directory server configuration, which can cause the IMS Server deployment to fail. 

Tips when configuring the directory server: 

- v The administrative user name that you supply for the WebSphere administrator must not exist on the directory server. Delete the user name from the Active Directory. 

- v Avoid creating an administrative user with the same user name as the WebSphere administrator. For example, if the WebSphere administrator you provide is wasadmin, then the user wasadmin must not exist on the corporate enterprise directory. 

- v Avoid using _administrator_ as the WebSphere Application Server administrator. 

- v Choose a user name that is least likely to conflict with your potential existing enterprise directory users. 

- v If the directory server is using an SSL connection, remember to add the directory server SSL certificates to the WebSphere Application Server. See "Adding the directory server SSL certificate to WebSphere Application Server" in the _IBM Security Access Manager for Enterprise Single Sign-On Installation Guide_ . 

- v After configuring the directory server, restart the WebSphere Application Server immediately to apply the configuration changes. If you configure the web server definition and the directory server before restarting the WebSphere Application Server, the configuration is not saved. 

- v Ensure that the directory server repositories are running, and you can connect to these repositories. If one or more of the configured repositories are unreachable, you cannot authenticate or stop the WebSphere Application Server. 

This issue is because of a security feature of the virtual member manager. The virtual member manager always checks all repositories before authenticating the user. For more information about the solution, see http:// publib.boulder.ibm.com/infocenter/wasinfo/v7r0/index.jsp?topic=/ com.ibm.websphere.wim.doc/ 

UnableToAuthenticateWhenRepositoryIsDown.html 

- v The NetBIOS name is not validated. You must provide the correct name. 

- v To determine the correct NetBIOS computer name, go to the Microsoft website at www.microsoft.com and search for “nbtstat”. See instructions on how to use **nbtstat** to determine the NetBIOS computer name. 

## **Node federation failed** 

You federate nodes to create a cluster on which you deploy the IMS Server. 

The node federation can fail if: 

**24** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Deployment Manager is not started** 

Before you federate the nodes again, ensure that the Deployment Manager is started. 

## **The node has a higher fix pack level than the Deployment Manager** 

Do not apply a WebSphere Application Server fix pack level that is higher than the Deployment Manager fix pack level. 

## **The nodes or the Deployment Manager cannot be reached.** 

There must be a two-way connection between the federated node and the Deployment Manager, and among the nodes. Each node must be able to contact the other nodes and the Deployment Manager. 

Use the **ping** command to check the connection. 

## **Cannot authenticate when a repository is down** 

If one or more of the configured repositories are down, you cannot authenticate or stop the WebSphere Application Server. 

**Symptom:** The following exception is displayed: 

CWWIM4520E The ’javax.naming.CommunicationException: Extdomain1.altext.ibm.com:389 [Root exception is java.net.ConnectException: Connection refused: connect]’ naming exception occurred during processing. at com.ibm.ws.wim.adapter.ldap.LdapConnection.reCreateDirContext (LdapConnection.java:613) at com.ibm.ws.wim.adapter.ldap.LdapConnection.search(LdapConnection.java:2419) 

## **Solution:** 

For more information about this problem and its possible solutions, see the following references: 

- v http://publib.boulder.ibm.com/infocenter/wasinfo/v7r0/index.jsp?topic=/ com.ibm.websphere.wim.doc/ 

   - UnableToAuthenticateWhenRepositoryIsDown.html 

- v http://publib.boulder.ibm.com/infocenter/wasinfo/v7r0/index.jsp?topic= %2Fcom.ibm.websphere.nd.doc%2Finfo%2Fae%2Fae 

   - %2Frxml_atidmgrrealmconfig.html 

## **IMS Server cannot issue a certificate for an application** 

The IMS Server cannot issue SCR or CAPI certificates for an authentication service with ID that contains the underscore (_) character. 

Subject fields of the IMS Server certificates cannot contain the underscore (_) character because it can cause problems at deployments that use certificate authentication for applications. 

Remove all underscore (_) characters from the authentication services IDs that use certificate authentication. 

## **Policy pid_ts_logon_cache_enabled is not displayed** 

The policy pid_ts_logon_cache_enabled is not displayed on the AccessAdmin UI. 

Chapter 4. Known problems and solutions **25** 

## **About this task** 

If you enabled this policy in the earlier version of the IMS Server and you upgraded to IMS Server 8.2, you cannot configure this policy in the AccessAdmin UI. Use this procedure to enable this policy in IMS Server 8.2. 

## **Procedure** 

1. Navigate to the policyConfig.xml file located in <WAS_Profile_Dir>/config/ tamesso/config/. 

2. Replace <!-- <value xml:lang="en">pid_ts_logon_cache_enabled</value> --> with <value xml:lang="en">pid_ts_logon_cache_enabled</value>. 

## **AccessProfile is not displayed in the properties pane** 

When you open an AccessProfile in AccessStudio, the content is supposed to be displayed on the properties pane. 

This problem is intermittent. 

**Symptom:** Nothing is displayed on the properties pane when you open an AccessProfile in AccessStudio 8.2 and you click the AccessProfile. 

**Solution:** Resize the **AccessStudio** window. 

## **AccessStudio might crash when you use the Convert to option** 

AccessStudio might crash when you open an AccessProfile for a web application and use the **Convert to** option to convert a trigger. This problem occurs when the web application is running either on Microsoft Internet Explorer or on Mozilla Firefox. 

**Symptom:** In AccessStudio, when you right-click a trigger and select **Convert to** any other trigger, you are prompted that an unhandled exception occurred in your application. 

**Solution:** Instead of using the **Convert to** option, use this procedure. 

1. Add a trigger. 

2. Copy the trigger details from the existing trigger into the new trigger. 

3. Delete the existing trigger. 

## **Cannot single sign-on in a command prompt** 

When you install AccessAgent, the console application support is not enabled by default. As such, you cannot single sign-on to a command prompt. 

To enable console application support, use SetupHlp.ini or execute InstallConsoleSupport.vbs. 

## **Enable console application support in SetupHlp.ini** 

Enable console application support in SetupHlp.ini during the AccessAgent installation. 

1. In the AccessAgent installer, open the Config folder. 

2. Double-click SetupHlp.ini to open the configuration settings file. 

**26** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

3. Under the Setup time only options category, set the value of ConsoleAppSupportEnabled to 1. 

## **Run InstallConsoleSupport.vbs** 

InstallConsoleSupport.vbs is automatically installed in the AccessAgent installation directory during the AccessAgent installation. 

If you have AccessAgent installed and you want to enable console application support, complete the following procedure. 

1. Run the InstallConsoleSupport.vbs. 

   - **Note:** Ensure that you have Administrator privileges before you run the script. 

2. Restart the computer. 

## **OutOfMemory error when opening an AccessProfile** 

AccessStudio 8.2 cannot handle large sizes of AccessProfiles. 

**Symptom:** If you open an AccessProfile with a size of 9 MB or larger, a System Out of Memory Exception occurs. 

**Solution:** Reduce the AccessProfile file size. 

## **Slow performance, startup and logon failure** 

If performance is slow for AccessAgent or the IMS Server, or if logon or startup fails for AccessAgent, the issue might be caused by an installed antivirus software. 

## **About this task** 

An antivirus software can cause: 

- v Slower AccessAgent performance on the user computer, and Citrix/Terminal Server. 

- v AccessAgent startup failure on the user computer, and Citrix/Terminal Server. 

- v Intermittent AccessAgent logon failure on the Citrix/Terminal Server. 

- v Slower IMS Server performance. 

To resolve these problems, include the IBM Security Access Manager for Enterprise Single Sign-On folders in the exclusion list of the antivirus software. Use the following procedure if you use McAfee antivirus. 

## **Procedure** 

1. Open the property pages of your antivirus scanner. 

2. On the **Detection** tab, under **What not to scan** , use the exclusions feature. 

3. Click **Exclusions** to open the **Set Exclusions** dialog box. 

4. Add files, folders, or drives or edit an item in the list. 

5. To add an item, click **Add** to open the **Add Exclusion Item** dialog box. 

6. Under **What to exclude** , select the folder by using **By name/location** . 

7. Under **When to exclude** , specify all options. 

8. Click **OK** to save these settings and return to the **Set Exclusions** dialog box. 

9. Click **OK** to save these settings and return to the **Detection** tab. 

10. Click **Apply** to save these settings. 

Chapter 4. Known problems and solutions **27** 

**Note:** If this solution does not improve the performance of your computer, upgrade the antivirus software to the latest version. If the problem persists after the upgrade, uninstall the antivirus software for troubleshooting or as a temporary solution. 

## **Browser-related issues** 

You can encounter issues while using your browser. 

See this topic for the issues and workarounds: 

- v “File download fails when using a Microsoft Internet Explorer browser.” 

- v “Microsoft Internet Explorer crashes” 

- v “Mozilla Firefox interferes with the AccessAgent single sign-on feature” on page 29 

- v “Single sign-on does not work in Mozilla Firefox” on page 29 

- v “Cannot capture logon credentials in Mozilla Firefox pop-up window” on page 30 

- v “Cannot launch web applications” on page 30 

- v “Back button does not work” on page 30 

## **File download fails when using a Microsoft Internet Explorer browser.** 

When you download a file from any web site, the browser stops responding and download fails. This problem occurs on Microsoft Internet Explorer version 7.0 and 8.0. 

**Solution:** Edit the Microsoft Internet Explorer AccessProfile to temporarily disable the Browser Helper Object. 

**Note:** Make sure that you have Administrator privileges, before you perform the following steps to resolve this issue. 

1. Launch AccessStudio. 

2. Click **File** -> **Import Data from IMS** to import the AccessProfile from the IMS Server. 

3. On the AccessProfiles list, click sso_site_wnd_iexplore profile. The different states and properties are displayed. 

4. Expand the trigger that is executed during the state transition from state_start to state_deactivate_bho. 

5. Click the **Window is Activated** trigger. 

6. Expand the **Conditions property** . 

7. In the VBScript code, change the line DisableBHOAtDownload = 0 to DisableBHOAtDownload = 1 

8. Save the **AccessProfile** . 

9. On the AccessProfiles list, right-click sso_site_wnd_iexplore profile and select **Upload to IMS** . 

## **Microsoft Internet Explorer crashes** 

Microsoft Internet Explorer crashes when you browse to any random web site. The problem occurs on Microsoft Internet Explorer version 7.0 and 8.0 and on any random web site. 

**28** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

**Solution:** Create an AccessProfile for the web site and specify whether to enable or not enable the Browser Helper Object. 

**Note:** Make sure that you have Administrator privileges, before you perform the following steps to resolve this issue. 

1. Launch AccessStudio. 

2. Create a basic AccessProfile for the website that displays this error. 

3. Enable **state editing** . 

4. Create a new state. For example: newstate1. 

5. Insert a trigger Fire immediately from the start state to newstate1. 

6. Add an action Run VBScript or JScript. 

7. Paste the following code in the script: dim objBHO objBHO = runtime.getBrowserObject() objBHO.enableBHO(false) 

8. Create another new state. For example: newstate2 

9. Insert a trigger Fire after specified time from newstate1 to newstate2. 

10. Set the trigger timeout to be as long as it takes to load the web page. 

11. Add an action Run VBScript or JScript 

12. Paste the following code in the script: dim objBHO objBHO = runtime.getBrowserObject() objBHO.enableBHO(true) 

13. Upload the new AccessProfile to the IMS Server. 

## **Mozilla Firefox interferes with the AccessAgent single sign-on feature** 

When you use Mozilla Firefox to log on to an application, Mozilla Firefox and AccessAgent both display a form to save the password. 

By default, the **Remember passwords for sites** option is enabled in Mozilla Firefox. This feature captures your password so that every time you log on to a Web site, your password is automatically entered. When AccessAgent captures your logon credentials, Mozilla Firefox also displays another form to save the password. 

During the AccessAgent installation, the installer automatically disables the **Remember passwords for sites** option in Mozilla Firefox. However, if you have not yet logged on to the Windows desktop and have not yet used Mozilla Firefox before, manually disable this option. 

To disable this feature in Mozilla Firefox: 

1. Launch the Mozilla Firefox. 

2. Navigate to **Tools** > **Options** > **Security** > **Passwords** . 

3. Clear the **Remember passwords for sites** check box. 

Alternately, go to C:\Program Files\IBM\ISAM ESSO\AA folder on your machine and double-click InstallFirefoxXpCom.vbs. 

## **Single sign-on does not work in Mozilla Firefox** 

Mozilla Firefox must be installed before AccessAgent. Otherwise, single sign-on does now work on Mozilla Firefox. 

**Symptom:** Single sign-on does not work in Mozilla Firefox. 

Chapter 4. Known problems and solutions **29** 

**Solution:** If AccessAgent is installed before Mozilla Firefox, navigate to C:\Program Files\IBM\ISAM ESSO\AA and run the InstallFirefoxXPCOM.vbs batch script. This script enables Mozilla Firefox to support single sign-on. 

## **Cannot capture logon credentials in Mozilla Firefox pop-up window** 

AccessAgent cannot capture the logon credentials in the Mozilla Firefox pop-up window. 

**Symptom:** In some Web page authentication, you are prompted to enter your user name and password in a pop-up window. If you are using Mozilla Firefox, AccessAgent cannot capture your input and detects the action trigger in the pop-up window. 

**Solution:** Use this procedure to capture your logon credentials. 

1. Use the **Window is activated** trigger to detect the basic authentication window pop-up event. 

2. Under this trigger, use the **Advanced Actions** > **Show a dialog to capture logon credentials** . 

## **Cannot launch web applications** 

You cannot launch web applications in Microsoft Internet Explorer if your browser is set to work offline. 

**Symptom:** If you launch a Microsoft Internet Explorer window and a network connection-related message is displayed, Microsoft Internet Explorer might be set to offline mode. 

**Solution:** Verify whether the Microsoft Internet Explorer is set to work offline by selecting the **File** menu from the Microsoft Internet Explorer. If the **Work Offline** option is selected, you cannot connect to the Internet. Clear the **Work Offline** option to resolve this issue. 

## **Back button does not work** 

The **Back** button does not work for AccessAdmin, AccessAssistant, and Web Workplace. 

You cannot use the **Back** button in a Web browser when you are using AccessAdmin, AccessAssistant, and Web Workplace. 

AccessAssistant and Web Workplace are designed this way because of security reasons, whereas AccessAdmin is designed this way because of certain implementation constraints. 

## **Verifications** 

This section covers some tips on how to verify versions, modes, and the type of deployment used. 

See the following topics: 

- v “Determining the type of IMS Server deployment” on page 31 

- v “Determining the Server AccessAgent mode” on page 31 

**30** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Determining the type of IMS Server deployment** 

If you want to know how the IMS Server is deployed, whether using the virtual appliance or the standard process, check the profile name and the operating system or check the Integrated Solutions Console. 

## **Using the profile name and operating system.** 

Check the System.Out log file. This log file indicates the profile name and the operating system. 

Within the environment variables printed at the beginning for each log file, locate: 

user.install.root = /opt/IBM/WebSphere/Profiles/DefaultAppSrv01 

For a virtual appliance deployment, the profile name is always **DefaultAppSrv01** and the operating system is SUSE Linux Enterprise Server. 

## **Using the Integrated Solutions Console** 

For a virtual appliance deployment, click the Welcome link, and it shows an entry for both the WebSphere Application Server and WebSphere HyperVisor. Otherwise, it just shows WebSphere Application Server. 

## **Verifying the IMS Server version** 

From the AccessAdmin navigation panel, select **System** > **Status** to view the system status, such as the server availability and version number. 

## **Determining the Server AccessAgent mode** 

If you want to know whether the Server AccessAgent is running in standard or lightweight mode, check the logs. 

To find out the lightweight mode setting on the server, use log level 3. Verify the log from TSVCServer.exe, with the following message: 

Lightweight mode AccessAgent disabled or Client AccessAgent has no V3 message support. 

To determine whether the session is running on lightweight mode, verify the log from TSVCServer.exe, with the following message: 

## **"Launch AATray success."** 

You are running in standard mode. 

## **"Not launching AATray."** 

You are running in lightweight mode. 

Chapter 4. Known problems and solutions **31** 

**32** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Chapter 5. Fixes** 

You can obtain fixes from the product support Web site and sign-up for notifications of product support information, including fixes. 

## **Obtaining fixes** 

A product fix might be available to resolve your problem. Check the product support site to determine what fixes are available for IBM Security Access Manager for Enterprise Single Sign-On. 

## **Before you begin** 

You can determine what fixes are available for IBM Security Access Manager for Enterprise Single Sign-On by checking the product support Web site: 

## **Procedure** 

1. Go to the IBM Software Support Web site for IBM Security Access Manager for Enterprise Single Sign-On: http://www.ibm.com/software/sysmgmt/ products/support/index.html 

2. Select **IBM Security Access Manager for Enterprise Single Sign-On** from the **Support for specific Tivoli products** drop-down list. A list of most recent fixes is listed in the Download section of the page. 

3. Click the name of a fix to read the description. You can also download the fix. 

## **Receiving fix notifications** 

Enable email notifications and subscriptions to receive notifications about any new fix packs and other news about IBM products. 

## **Procedure** 

To receive email notifications about fixes and other news about IBM products, follow these steps: 

1. Go to the IBM Software Support Web site for IBM Security Access Manager for Enterprise Single Sign-On: http://www.ibm.com/software/sysmgmt/ products/support/index.html 

2. Select **IBM Security Access Manager for Enterprise Single Sign-On** from the **Support for specific Tivoli products** drop-down list. 

3. Click **My Support** in the upper-right corner of the page. A sign-in page is displayed. 

4. If you have already registered, go to the next step. If you have not registered, click **Register now** to establish your user ID and password. 

5. Sign in to **My support** . 

6. Click the **Edit profile** tab. 

7. Select **Software** > **Security** > **Access** in the fields that are displayed. 

8. Select **IBM Security Access Manager for Enterprise Single Sign-On** from the list of products displayed. 

9. Click **Add products** . 

**33** 

© Copyright IBM Corp. 2002, 2012 

10. To enable email notification, click **Subscribe to email** at the top of the page. 

11. From the list, click **Software** . 

12. Select the check boxes that best describe the email notifications that you would like to receive. 

13. Click **Update** . 

14. Sign out of the session by clicking **Sign out** or click **Go to my personalized page** to see your personalized support page. 

**34** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Chapter 6. Searching knowledge bases** 

IBM Support for IBM Security Access Manager for Enterprise Single Sign-On maintains a knowledge base of technical documentation, problems, and workarounds. 

## **About this task** 

IBM Support Assistant includes a hierarchical search tool to help you focus your search for information related to a specific product, platform, or issue. See “IBM Support Assistant” on page 49 for more information. 

The following procedure describes how to perform a manual search for information. 

## **Procedure** 

1. Go to the IBM Software Support Web site for IBM Security Access Manager for Enterprise Single Sign-On: http://www.ibm.com/software/sysmgmt/ products/support/index.html 

2. Select **IBM Security Access Manager for Enterprise Single Sign-On** from the **Support for specific Tivoli products** drop-down list. 

3. Under **Solve a problem** , click any of the following options: 

   - v **Technotes** , which lists information about the product by article title. 

   - v **APARs** , which lists known problems according to Authorized Program Analysis Report numbers. 

4. Optionally, search for specific terms, error codes, or APARs by using the **Search** field on the product support page. You can also browse through the Technotes or APARs pages. 

**35** 

© Copyright IBM Corp. 2002, 2012 

**36** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Chapter 7. Analyzing data** 

After you collect data from multiple sources, you must determine how that data can help you to resolve your problem. 

To analyze the data, take the following actions: 

- v Determine which data sources are most likely to contain information about the problem, and start your analysis from those sources. For example, if the problem is related to installation, start your analysis with the installation log files, if any. This action helps narrow down the problem, instead of starting with the general product or operating system log files. 

- v Understand how the various pieces of data relate to each other. For example, if the data spans to more than one system, keep your data organized to know which pieces of data come from which sources. 

- v Use timestamps to confirm that each piece of diagnostic data is relevant to the timing of the problem. 

**Note:** Data from different sources can have different timestamp formats. Understand the sequence of the different elements in each timestamp format so you can tell when the different events occur. 

The specific method of analysis is unique to each data source. One tip that is applicable to most traces and log files is to start by identifying the point in the data where the problem occurs. After you identify that point, go through the data to trace the root cause of the problem. 

To investigate a problem for which you have comparative data for a working and non-working environment, start by comparing the operating system and product configuration details for each environment. 

**37** 

© Copyright IBM Corp. 2002, 2012 

**38** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Chapter 8. Collecting data** 

There are other ways to solve a problem aside from troubleshooting the symptoms. Another way of solving a problem is collecting more diagnostic data. 

Before you begin to collect data for a problem report, install and run the IBM Support Assistant. This troubleshooting tool includes a console where you can submit an online problem management record (PMR). As part of the process, information specific to your system, environment, and product is gathered into a file used by IBM Software Support. For more information about IBM Support Assistant, see “IBM Support Assistant” on page 49. 

Collecting data early, even before opening a problem management record (PMR), can help you to answer the following questions: 

1. Do the symptoms match any known problems? 

2. If so, has a fix or workaround been published? 

3. Is the problem a non-defect-oriented problem that can be identified and resolved without a code fix? 

4. Where does the problem originate? 

The diagnostic data that you need to collect and the sources from which you collect that data are dependent on the type of problem that you are investigating. 

For help identifying the component from which the problem originates, follow the questions in the troubleshooting checklist for IBM Security Access Manager for Enterprise Single Sign-On. 

## **Collecting general data** 

When you submit a problem to IBM Software Support, there is a base set of information that you typically must provide details about the affected system or systems, such as: 

- v Version of IBM Security Access Manager for Enterprise Single Sign-On and patch levels on affected systems. 

- v Operating system name and version. 

- v General details about the structure of your environment, such as number of servers and software installed, domains and federations configured, and so on. 

## **Collecting problem-specific data** 

For specific symptoms, or for problems in a specific part of the product, you must collect additional data, such as message and trace information. See “Message and trace logs” for more information. After you collect the appropriate diagnostic data, you can attempt to analyze the data yourself or you can provide it to IBM Software Support. 

## **Message and trace logs** 

IBM Security Access Manager for Enterprise Single Sign-On message and trace logs are managed and stored by WebSphere Application Server. 

**39** 

© Copyright IBM Corp. 2002, 2012 

See the troubleshooting topics in the WebSphere Application Server information center for detailed information about logs and logging. 

## **Message logs** 

Message logs are text files in which the operations of the system are recorded. 

The following types of messages are recorded by default: 

## **Informational messages** 

Indicate conditions that are worthy of noting but that do not require you to take any precautions or perform an action. 

## **Warning messages** 

Indicate that a condition has been detected that you must be aware of, but does not necessarily require any action. 

## **Error messages** 

Indicate that a condition has occurred that requires an action. 

## **Message log files** 

All IBM Security Access Manager for Enterprise Single Sign-On messages are logged in the following default WebSphere Application Server message logs. 

_Table 2. Message logs_ 

|**Log**||||**Default **|**file name**|**Content**||||
|---|---|---|---|---|---|---|---|---|---|
|JVM|Logs|||SystemOut.log||Messages in text format for||||
|||||||the application server||||
|||||||instance.||||
|IBM|Service||Log|activity.log||Messages in binary Common||||
|||||||Base Event format for the||||
|||||||application server||||
|||||||installation.||||
|||||||**Note:** Tools for viewing this||||
|||||||format are provided with||||
|||||||WebSphere Application||||
|||||||Server. See the WebSphere||||
|||||||Application Server||||
|||||||information center for more||||
|||||||information.||||

You can use the WebSphere Application Server administrative consoleto configure the following log settings: 

- v location 

- v name 

- v maximum size of the log files 

- v levels of severity that you want to log, such as Warning and Severe 

See “Configuring log settings” on page 42 for more information. 

**40** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Message log locations** 

By default, the message logs are located in the following directories. 

_Table 3. Application server default message log locations_ 

|**Log**||**Path**||||
|---|---|---|---|---|---|
|JVM Logs||**Windows:**||||
|||C:\Program Files\IBM\WebSphere\AppServer\profiles\||||
|||_profile_name_\ logs\_server_name_\SystemOut.log||||
|IBM Service Log||**Windows:**||||
|||C:\Program Files\IBM\WebSphere\AppServer\profiles\||||
|||_profile_name_\ logs\_server_name_\activity.log||||
|HTTP Server Log<br>C:\Program Files\IBM\HTTPServer\logs||||||
|ISAM ESSO Log||C:\Program Files\IBM\ISAM ESSO\Logs||||

Console message logs are saved in the message log directories of the WebSphere Application Server node where the administration console is installed. 

## **Trace logs** 

Trace logging, or tracing, provides IBM Software Support personnel with additional information relating to the condition of the system at the time a problem occurred. 

Trace logs capture transient information about the current operating environment when a component or application fails to operate as intended. Trace logs are different from message logs because message logs records only the occurrence of noteworthy events. Trace logs are available only in English. 

Trace logging is not enabled by default. In some circumstances, trace logging might cause large amounts of data to be collected in a short amount of time which results in significant performance degradation. Therefore, enable the trace logging only at the direction of IBM Software Support personnel. See “Configuring log settings” on page 42 for more information. 

Trace log entries can provide the following level of detail: 

**Fine** Minimal detail. 

**Finer** Moderate detail. **Finest** Maximum (verbose) detail. 

## **Trace log file** 

If tracing is enabled for an application server, IBM Security Access Manager for Enterprise Single Sign-On trace information is logged in the following default WebSphere Application Server trace log. 

_Table 4. Trace log_ 

||**Default log name**<br>**Default file name**<br>**Content**<br>Diagnostic Trace<br>trace.log<br>Trace information in text<br>format for the application<br>server instance.|
|---|---|

Chapter 8. Collecting data **41** 

Using the WebSphere Application Server administrative console, you can configure some settings of the logs, such as the location, name, maximum size of the log files and the level of detail that you want to log (such as Fine, Finer, Finest). For more information, refer to “Configuring log settings.” 

## **Trace log locations** 

By default, the trace log is located in the following directories. 

_Table 5. Application server default trace log locations_ 

||**Log**<br>**Path**<br>Diagnostic Trace<br>**UNIX and Linux:**<br>/opt/IBM/WebSphere/AppServer/profiles/_profile_name_/logs/<br>_server_name_/trace.log<br>**Windows:**<br>C:\Program Files\IBM\WebSphere\AppServer\profiles\<br>_profile_name\_logs\_server_name_\trace.log|
|---|---|

Console trace logs are saved in the trace log directories of the WebSphere Application Server node where the administration console is installed. 

## **Configuring log settings** 

You can use the administration console to configure the settings for message and trace logs. Message logging is enabled by default. Trace logging must be enabled only at the direction of IBM Support personnel. 

## **Configuring message logging** 

Message logging to the JVM log and the IBM Service log is enabled by default. Both logs are configured to log messages for all IBM Security Access Manager for Enterprise Single Sign-On components of all severity levels. You can modify the names, location, file size, and severity level to be logged. 

## **Configuring the JVM log** 

You can modify the file name, location, file format, file size, logging start and stop times, number of logs to keep, and severity level to be logged in the JVM Log. 

## **About this task** 

The JVM log, also called as SystemOut.log, is a standard WebSphere Application Server log used for messages. For detailed information, see the JVM log topics in the WebSphere Application Server information center. 

## **Procedure** 

1. Start the WebSphere Application Server administrative console and log on, if necessary. 

2. Click **Troubleshooting** > **Logs and Trace** to open the Logging and Tracing page. 

3. Click the name of the server that you want to configure. For example, server1. 

4. Click **JVM Logs** to view the configuration options. 

5. Select the **Configuration** tab. 

**42** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

6. Scroll through the panel to show the attributes to configure. 

7. Change the appropriate configuration attributes. 

8. Click **Apply** . 

9. Save your configuration changes. 

## **Configuring the IBM Service log** 

The IBM Service log is enabled by default. You can change this setting or modify the names, location, file size, and severity level to be logged in the log. 

## **About this task** 

The service log, also called as the activity.log, is a standard WebSphere Application Server log used for messages. For detailed information about the log, refer to the service log topics in the WebSphere Application Server information center. 

## **Procedure** 

1. Start the WebSphere Application Server administrative console and log on, if necessary. 

2. Click **Troubleshooting** > **Logs and Trace** to open the Logging and Tracing page. 

3. Double-click the name of the server that you want to configure. For example, server1. 

4. Click **IBM Service Logs** to view the configuration options. 

5. Select or clear the **Enable service log** box to enable or disable logging. The service log is enabled by default. 

6. Set the name for the service log in the **File Name** field. The default name is activity.log. If the name is changed, the runtime requires write access to the new file, and the file must use the .log extension. 

7. Specify the number of megabytes to which the file can grow in the **Maximum File Size** field. When the file reaches this size, it wraps, replacing the oldest data with the newest data. 

8. Click **Apply** to save the configuration changes. 

9. Restart the server for the configuration changes to take effect. 

## **Enabling trace logging** 

You can enable trace logging at server startup or on a running server. To maintain system performance, enable trace logging only at the direction of IBM Support personnel. 

## **Enabling trace at server startup** 

Trace logging can be enabled at server startup. 

## **About this task** 

The trace log is a standard WebSphere Application Server log used for trace information. For detailed information about the log, see the WebSphere Application Server information center. 

## **Procedure** 

1. Start the WebSphere Application Server administrative console and log on, if necessary. 

Chapter 8. Collecting data **43** 

2. Click **Troubleshooting** > **Logs and Trace** to open the Logging and Tracing page. 

3. Click the name of the server that you want to configure, for example, server1. 

4. Click **Diagnostic Trace** to view the configuration options. 

5. Click the **Configuration** tab. 

6. Select or clear the **Enable log** box to enable or disable logging. The trace log is disabled by default. 

7. Complete the configuration as instructed by IBM Support personnel. For additional information about the configuration settings, see the troubleshooting and trace log topics in the WebSphere Application Server information center. 

8. Click **Apply** to save your configuration changes. 

9. To enter a trace string to set the trace specification to the required state: 

   - a. Click **Troubleshooting** > **Logs and Trace** to open the Logging and Tracing page. 

   - b. Click the server you want to configure, for example, server1. 

   - c. Click **Change Log Detail Levels** . 

   - d. If the **All Components** option has been enabled, you turn it off and then enable specific components. 

10. Click a component or group name. 

11. Enter a trace string in the trace string box. For more information about trace strings, see the WebSphere Application Server information center. 

12. Click **OK** . 

13. Click **Save** to save your changes. You must restart WebSphere Application Server for the change to take effect. 

## **Enabling trace on a running server** 

Trace logging can be enabled on a running server. 

## **About this task** 

The trace log is a standard WebSphere Application Server log used for trace information. For detailed information about the log, see the WebSphere Application Server information center. 

## **Procedure** 

1. Start the WebSphere Application Server administrative console and log on, if necessary. 

2. Click **Troubleshooting** > **Logs and Trace** to open the Logging and Tracing page. 

3. Click the name of the server that you want to configure, for example, server1. 

4. Click **Diagnostic Trace** . 

5. Click the **Runtime** tab. 

6. Select the **Save runtime changes to configuration as well** box if you want to write your changes back to the server configuration. 

7. Change the existing trace state by changing the trace specification to the required state. 

8. Configure the trace output if you want to change the existing one. 

9. Click **Apply** . 

**44** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Viewing logs** 

The format of the logs determines how they can be viewed. 

## **JVM logs** 

You can view the JVM logs with any of the following options: 

- v Use the WebSphere Application Server administrative console, which also supports viewing from a remote machine 

- v Use a text editor on the machine where the log files are stored. 

See the **Viewing JVM logs** section in the WebSphere Application Server information center for more information. 

## **Using IBM Support Assistant** 

The IBM Support Assistant tool helps troubleshoot IBM Security Access Manager for Enterprise Single Sign-On. Use the tool to automatically collect problem data. 

You must install the IBM Security Access Manager for Enterprise Single Sign-On plug-in for IBM Support Assistant as part of the IBM Security Access Manager for Enterprise Single Sign-On installation. If you did not specify the IBM Support Assistant component when installing the product, install it now. 

- To use the tool, see the following topics: 

- v “Using the IBM Support Assistant in graphical mode” 

- v “Using the IBM Support Assistant in console mode” on page 46 

## **Using the IBM Support Assistant in graphical mode** 

You can use a graphical user interface to collect data with IBM Support Assistant. 

## **About this task** 

To access the graphical user interface, run a script from the command line. 

## **Procedure** 

1. Ensure that your Java environment is configured correctly: 

   - a. Verify that your Java runtime environment is at level 1.4.2 or higher. 

   - b. Determine if the location of the Java runtime environment is included in your PATH environment setting. If the location is not included in your path, set the variable JAVA_HOME to point to the Java runtime environment. 

_Table 6. Specifying JAVA_HOME for your environment_ 

||**Operating system**<br>**Sample command**<br>Windows<br>For example, if you have a Java Development Kit installed<br>at c:\jre1.4.2, use the command:<br>SET JAVA_HOME=c:\jre1.4.2|
|---|---|

2. Start the IBM Support Assistant tool: 

   - Open a command window, and change directory to the ISAlite installation directory. Enter the command runISALite.bat. The IBM Support Assistant now starts a graphical user interface. 

3. In the Problem Type window, select a problem type. 

Chapter 8. Collecting data **45** 

Expand the folders to display all problem types. Find your problem type and select it. 

4. Supply a filename for the data collection .zip file. You can use any filename. The tool automatically appends the .zip file extension. For example, if you enter the filename Install_problem, the file is named Install_problem.zip. 

## 5. Click **Collect Data** . 

The collection script runs and prompts you for additional information. The information can include configuration information or, the sequence of events leading to the problem. The script might also prompt you for preferences for data collection. 

When the scripts finishes collecting the setup information, it collects the necessary data. The tool creates a .zip file that you can send to IBM Support. 

6. When prompted, enter a filename in the **Output Filename/Path** box. 

The tool appends the server hostname and current timestamp to the filename that you entered. 

7. Send the .zip file to IBM Support 

You can choose FTP or HTTPS for file transfer. 

**Note:** FTP is not encrypted and HTTPS is encrypted. 

## **Using the IBM Support Assistant in console mode** 

You can collect data with IBM Support Assistant in console mode. 

## **About this task** 

Console mode provides command-line control of the IBM Support Assistant Lite collection scripts. The tool lets you record your responses from a console-mode session in a response file. You can then use the response file to drive subsequent executions of the same collection script. 

## **Procedure** 

1. Ensure that your Java environment is configured correctly: 

   - a. Verify that your Java runtime environment is at level 1.4.2 or higher. 

   - b. Determine if the location of the Java runtime environment is included in your PATH environment setting. If the location is not included in your path, set the variable JAVA_HOME to point to the Java runtime environment. 

_Table 7. Specifying JAVA_HOME for your environment_ 

||**Operating system**<br>**Sample command**<br>Windows<br>For example, if you have a Java Development Kit installed<br>at c:\jre1.4.2, use the command:<br>SET JAVA_HOME=c:\jre1.4.2|
|---|---|

2. Start the IBM Support Assistant tool: 

Open a command window, and change directory to the ISAlite installation directory. The IBM Support Assistant now starts in console mode. 

3. Create a response file by using the following command runISALiteConsole.bat -record _response.txt_ . 

You can specify your own filename for _response.txt_ . 

**46** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

When running in this mode, you supply data input during an interactive session. The tool records your responses into the file that you specify. 

4. Run the tool by using the response file that you have created runISALiteConsole.bat _response.txt_ . Notes[®] : 

   - v The response file is a plain text file. You can edit it to modify values as needed. For example, you can use the file on another computer after adjusting the response file values to reflect settings for the local computer. 

   - v Remember that sensitive information, such as user names and passwords, might be stored in the response file. Manage the file carefully, to prevent unauthorized access to important information. 

   - v Some data collection sessions require interaction with the user, and thus are not suitable for the silent collection option. For example, IBM Support might ask you to reproduce a problem during data collection, in order to collect log and trace files. In this case, silent collection cannot record and reproduce all steps. 

Chapter 8. Collecting data **47** 

**48** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Chapter 9. Contacting support** 

IBM Software Support provides assistance with product defects. 

You can contact IBM Software Support in the following ways: 

- v **IBM Support Assistant:** You can search for information about a problem and collect the logged information required to troubleshoot a problem by using the IBM Support Assistant. You can use it to open a problem management report (PMR) online. It is also helpful to use the IBM Support Assistant to report a problem to IBM Software Support. You need your user account ID and password to submit a PMR through the IBM Support Assistant. The IBM Support Assistant client is included on your product CD and updates can be downloaded from the following website: http://www.ibm.com/software/support/isa/ 

- v **Online:** Go to the **Submit** and **track problems** tab on the IBM Software Support site at http://www.ibm.com/software/support/probsub.html. Type your information into the appropriate problem-submission tool. 

- v **By phone:** For the phone number to call in your country, go to the Contacts page of the _IBM Software Support Handbook_ at http://www14.software.ibm.com/ webapp/set2/sas/f/handbook/contacts.html, and click the name of your geographic region. 

If the problem that you submit is for a software defect, missing content, or inaccurate documentation, IBM Software Support creates an Authorized Program Analysis Report (APAR). The APAR describes the problem in detail. Whenever possible, IBM Software Support provides a workaround that you can implement until the APAR is resolved and a fix is delivered. IBM publishes resolved APARs on the Software Support website daily, so that other users who experience the same problem can benefit from the same resolution. 

Before you submit a problem to IBM Software support, answer these questions: 

1. Do you have an active IBM software maintenance contract? 

2. Do you understand the business effect of the problem? 

3. Can you describe the problem? 

## **IBM Support Assistant** 

IBM Support Assistant simplifies the process of researching and reporting on software problems. 

IBM Support Assistant provides quick access to support-related information along with serviceability tools for problem determination. IBM Support Assistant consists of three tools: 

## **Search** 

Use multiple filters to focus your search to access troubleshooting repository information quickly. The concurrent search tool spans the bulk of IBM documentation and returns results that are categorized by source for easy review. 

## **Product information links** 

These self help links include: 

v Product support pages 

**49** 

© Copyright IBM Corp. 2002, 2012 

- v Product home pages 

- v Product troubleshooting guides 

- v Product education road maps and the IBM Education Assistant 

- v Product updates 

- v Product news groups and forums 

## **Service feature** 

The service feature is an automated system collector and symptom-based collector. The system collector gathers general information from your operating system, registry, and other sources. The symptom-based collector gathers specific product information relating to a particular problem that you are having. Use the service feature to automatically set tracing to help IBM support in the data gathering process. 

The service feature also enables you to submit a problem online to IBM Software Support. Enter your entitlement information once, and save it for future sessions. You can then create a problem report for IBM and attach the gathered data in the collector file. 

IBM Support Assistant provides a complete online user guide to assist you in the setup and use of the tool. The following steps describe the basic procedure for setting up your system to use IBM Support Assistant: 

1. Install the IBM Support Assistant tool from your product CD, or from the following Web site: 

http://www.ibm.com/software/support/isa/ 

2. In an IBM software repository, locate the IBM Support Assistant plug-in for the version of WebSphere Application Server that you are running. The IBM Security Access Manager for Enterprise Single Sign-On plug-in uses the WebSphere Application Server plug-in as the base code. 

**Note:** Be patient downloading the WebSphere Application Server plug-in; it can take a long time depending on network traffic and the availability of system resources. 

3. Install the WebSphere Application Server plug-in into the \plugin subdirectory of the IBM Support Assistant installation directory. 

4. Locate the IBM Support Assistant plug-in for IBM Security Access Manager for Enterprise Single Sign-On on the product CD or in an IBM software repository. 

5. Install the IBM Support Assistant plug-in into the \plugin subdirectory of the IBM Support Assistant installation directory. 

6. Click your IBM Support Assistant desktop icon to start. Select the **User Guide** tab for information about performing the various available tasks. 

## **IBM software maintenance contracts** 

Ensure that your company has an active maintenance contract before you submit a problem to IBM Software Support. Make sure that you are also authorized to submit problems to IBM. 

If you are not sure what type of software maintenance contract you need, call 1-800-IBMSERV (1-800-426-7378) in the United States. From other countries, go to the Contacts page of the _IBM Software Support Handbook_ at http:// www14.software.ibm.com/webapp/set2/sas/f/handbook/contacts.html, and click the name of your geographic region for phone numbers of people who provide support for your location. 

**50** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Determining the business impact** 

When you submit a problem to IBM, you are asked to supply a severity level. Therefore, you must understand and assess the business impact of the problem that you are reporting. 

Use the following criteria: 

_Table 8. Severity levels_ 

||Severity 1<br>The problem has a _critical_ business impact: You are unable to use the<br>program, resulting in a critical impact on operations. This condition<br>requires an immediate solution.<br>Severity 2<br>This problem has a _significant_ business impact: The program is usable,<br>but it is severely limited.<br>Severity 3<br>The problem has _some_ business impact: The program is usable, but<br>less significant features (not critical to operations) are unavailable.<br>Severity 4<br>The problem has _minimal_ business impact: The problem causes little<br>impact on operations or a reasonable circumvention to the problem<br>was implemented.|
|---|---|

## **Describing a problem** 

When describing a problem to IBM, be as specific as possible. Include all relevant background information so that IBM Software Support specialists can help you solve the problem efficiently. 

To save time, know the answers to these questions: 

- v What software versions were you running when the problem occurred? 

- v Do you have logs, traces, and messages that are related to the problem symptoms? 

- v Can you re-create the problem? If so, what steps do you perform to re-create the problem? 

- v Did you change anything in the system? For example, did you change anything in the hardware, operating system, networking software, or other system components? 

- v Are you currently using a workaround for the problem? If so, be prepared to describe the workaround when you report the problem. 

## **Submitting data** 

You can send diagnostic data, such as log files and configuration files, to IBM Software Support. 

Use one of the following methods: 

- v IBM Support Assistant 

- v FTP (EcuRep) 

- v ESR tool 

## **IBM Support Assistant** 

IBM Support Assistant includes a service feature which has an automated system collector and a symptom-based collector. The system collector gathers general 

Chapter 9. Contacting support **51** 

information from your operating system, registry, and other sources. The symptom-based collector gathers specific product information relating to a particular problem that you are having. The service feature also enables you to automatically set tracing to help IBM support in the data gathering process. See the “IBM Support Assistant” on page 49 for more information about IBM Support Assistant. 

## **FTP (EcuRep)** 

Use the FTP service called EcuRep to submit data files to IBM. Package the data files that you collected into ZIP or TAR format, and name the package according to your Problem Management Record (PMR) identifier. Your file must use the following naming convention to be correctly associated with the PMR: 

xxxxx.bbb.ccc.yyy.yyy 

where: 

_Table 9. File naming convention_ 

||xxxxx<br>PMR number<br>bbb<br>Branch, from the PMR identifier<br>ccc<br>Country code, from the PMR identifier<br>yyy.yyy<br>File type (ZIP or TAR format)|
|---|---|

Use FTP to transfer your files and follow these steps: 

1. Using an FTP utility, connect to the emea.ibm.com server (for example, ftp.emea.ibm.com). 

2. Log on as anonymous. 

3. Enter your email address as your password. 

4. Change directories to toibm (for example, cd toibm). 

5. Change to one of the platform-specific subdirectories: aix, cae, hw, linux, lotus, mvs, os2, os400, swm, tivoli, unix, vm, vse, and windows. 

6. Change to binary (bin) mode (for example, bin). 

7. Put your file on the server. You can send but not update files on the FTP server. Therefore, any subsequent time that you must change the file, you create a file with a unique name. 

For more information about the EcuRep service, see IBM EMEA Centralized Customer Data Store Service at http://www.ibm.com/de/support/ecurep/ index.html. 

## **ESR tool** 

Registered users who are on an authorized caller list can use the Electronic Service Request (ESR) tool to submit diagnostic data. Use the ESR tool to submit and manage Problem Management Records (PMRs) on demand, 24 hours a day, seven days a week, 365 days a year. 

To submit data using ESR, complete these steps: 

1. Sign onto ESR. 

2. On the Welcome page, enter your PMR number in the **Enter a report number** field, and click **Go** . 

**52** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

3. Scroll down to the **Attach Relevant File** field. 

4. Click **Browse** to locate the log, trace, or other diagnostic file that you want to submit to IBM Software Support. 

5. Click **Submit** . Your file is transferred to IBM Software Support through FTP, and it is associated with your PMR. 

Chapter 9. Contacting support **53** 

**54** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Notices** 

This information was developed for products and services offered in the U.S.A. IBM may not offer the products, services, or features discussed in this document in other countries. Consult your local IBM representative for information on the products and services currently available in your area. Any reference to an IBM product, program, or service is not intended to state or imply that only that IBM product, program, or service may be used. Any functionally equivalent product, program, or service that does not infringe any IBM intellectual property right may be used instead. However, it is the user's responsibility to evaluate and verify the operation of any non-IBM product, program, or service. 

IBM may have patents or pending patent applications covering subject matter described in this document. The furnishing of this document does not give you any license to these patents. You can send license inquiries, in writing, to: 

IBM Director of Licensing IBM Corporation North Castle Drive Armonk, NY 10504-1785 U.S.A. 

For license inquiries regarding double-byte (DBCS) information, contact the IBM Intellectual Property Department in your country or send inquiries, in writing, to: 

Intellectual Property Licensing Legal and Intellectual Property Law IBM Japan, Ltd. 1623-14, Shimotsuruma, Yamato-shi Kanagawa 242-8502 Japan 

**The following paragraph does not apply to the United Kingdom or any other country where such provisions are inconsistent with local law :** 

INTERNATIONAL BUSINESS MACHINES CORPORATION PROVIDES THIS PUBLICATION "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. 

Some states do not allow disclaimer of express or implied warranties in certain transactions, therefore, this statement might not apply to you. 

This information could include technical inaccuracies or typographical errors. Changes are periodically made to the information herein; these changes will be incorporated in new editions of the publication. IBM may make improvements and/or changes in the product(s) and/or the program(s) described in this publication at any time without notice. 

Any references in this information to non-IBM Web sites are provided for convenience only and do not in any manner serve as an endorsement of those Web sites. The materials at those Web sites are not part of the materials for this IBM product and use of those Web sites is at your own risk. 

**55** 

© Copyright IBM Corp. 2002, 2012 

IBM may use or distribute any of the information you supply in any way it believes appropriate without incurring any obligation to you. 

Licensees of this program who wish to have information about it for the purpose of enabling: (i) the exchange of information between independently created programs and other programs (including this one) and (ii) the mutual use of the information which has been exchanged, should contact: 

IBM Corporation 2Z4A/101 11400 Burnet Road Austin, TX 78758 U.S.A. 

Such information may be available, subject to appropriate terms and conditions, including in some cases payment of a fee. 

The licensed program described in this document and all licensed material available for it are provided by IBM under terms of the IBM Customer Agreement, IBM International Program License Agreement or any equivalent agreement between us. 

Any performance data contained herein was determined in a controlled environment. Therefore, the results obtained in other operating environments may vary significantly. Some measurements may have been made on development-level systems and there is no guarantee that these measurements will be the same on generally available systems. Furthermore, some measurement may have been estimated through extrapolation. Actual results may vary. Users of this document should verify the applicable data for their specific environment. 

Information concerning non-IBM products was obtained from the suppliers of those products, their published announcements or other publicly available sources. IBM has not tested those products and cannot confirm the accuracy of performance, compatibility or any other claims related to non-IBM products. Questions on the capabilities of non-IBM products should be addressed to the suppliers of those products. 

All statements regarding IBM's future direction or intent are subject to change or withdrawal without notice, and represent goals and objectives only. 

All IBM prices shown are IBM's suggested retail prices, are current and are subject to change without notice. Dealer prices may vary. 

This information is for planning purposes only. The information herein is subject to change before the products described become available. 

This information contains examples of data and reports used in daily business operations. To illustrate them as completely as possible, the examples include the names of individuals, companies, brands, and products. All of these names are fictitious and any similarity to the names and addresses used by an actual business enterprise is entirely coincidental. 

## COPYRIGHT LICENSE: 

This information contains sample application programs in source language, which illustrate programming techniques on various operating platforms. You may copy, modify, and distribute these sample programs in any form without payment to 

**56** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

IBM, for the purposes of developing, using, marketing or distributing application programs conforming to the application programming interface for the operating platform for which the sample programs are written. These examples have not been thoroughly tested under all conditions. IBM, therefore, cannot guarantee or imply reliability, serviceability, or function of these programs. You may copy, modify, and distribute these sample programs in any form without payment to IBM for the purposes of developing, using, marketing, or distributing application programs conforming to IBM's application programming interfaces. 

If you are viewing this information in softcopy form, the photographs and color illustrations might not be displayed. 

## **Trademarks** 

IBM, the IBM logo, and ibm.com[®] are trademarks or registered trademarks of International Business Machines Corp., registered in many jurisdictions worldwide. Other product and service names might be trademarks of IBM or other companies. A current list of IBM trademarks is available on the Web at Copyright and trademark information; at www.ibm.com/legal/copytrade.shtml. 

Adobe, Acrobat, PostScript and all Adobe-based trademarks are either registered trademarks or trademarks of Adobe Systems Incorporated in the United States, other countries, or both. 

IT Infrastructure Library is a registered trademark of the Central Computer and Telecommunications Agency which is now part of the Office of Government Commerce. 

Intel, Intel logo, Intel Inside, Intel Inside logo, Intel Centrino, Intel Centrino logo, Celeron, Intel Xeon, Intel SpeedStep, Itanium, and Pentium are trademarks or registered trademarks of Intel Corporation or its subsidiaries in the United States and other countries. 

Linux is a trademark of Linus Torvalds in the United States, other countries, or both. 

Microsoft, Windows, Windows NT, and the Windows logo are trademarks of Microsoft Corporation in the United States, other countries, or both. 

ITIL is a registered trademark, and a registered community trademark of the Office of Government Commerce, and is registered in the U.S. Patent and Trademark Office. 

UNIX is a registered trademark of The Open Group in the United States and other countries. 

Java and all Java-based trademarks and logos are trademarks or registered trademarks of Oracle and/or its affiliates. 

Notices **57** 

Cell Broadband Engine is a trademark of Sony Computer Entertainment, Inc. in the United States, other countries, or both and is used under license therefrom. 

Linear Tape-Open, LTO, the LTO Logo, Ultrium, and the Ultrium logo are trademarks of HP, IBM Corp. and Quantum in the U.S. and other countries. 

Other company, product, and service names may be trademarks or service marks of others. 

**58** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Glossary** 

**AccessAdmin.** A web-based management console that Administrators and Helpdesk officers use to administer the IMS Server and to manage users and policies. 

**AccessAgent plug-in.** A piece of script, written in VBscript or Javascript, that is embedded within an AccessProfile to perform custom checking of conditions or to execute custom actions. It is used for extending the capability of an AccessProfile beyond the built-in triggers and actions. 

**AccessAgent.** The client software that manages the identity of the user, authenticates the user, and automates single sign-on and sign-off. 

**AccessAssistant.** The web-based interface that helps users to reset their passwords and retrieve their application credentials. 

**AccessProfile widget / widget.** An independent AccessProfile that consists of pinnable states, which can be used to build another AccessProfile. 

**AccessProfiles.** AccessAgent uses these XML specifications to identify application screens that it can perform single sign-on and automation. 

**AccessStudio.** An application used by Administrators for creating and maintaining AccessProfiles. 

**Account data bag.** A data structure that holds user credentials in memory while single sign-on is performed on an application. 

**Account data item template.** A template that defines the properties of an account data item. 

**Account data item.** The user credentials required for logon. 

**Account data template.** A template that defines the format of account data to be stored for credentials captured by using a specific AccessProfile. 

**Account data.** The logon information required to verify an authentication service. It can be the user name, password, and the authentication service which the logon information is stored. 

**Action.** In profiling, an act that can be performed in response to a trigger. For example, automatic filling of user name and password details as soon as a sign-on window displays. 

**Active Directory (AD).** A hierarchical directory service that enables centralized, secure management of an entire network, which is a central component of the Microsoft Windows platform. 

**Active Directory credentials.** The Active Directory user name and password. 

**Active Directory password synchronization.** An IBM Security Access Manager for Enterprise Single Sign-On feature that synchronizes the ISAM ESSO password with the Active Directory password. 

**Active RFID (ARFID).** ARFID is both a second authentication factor and a presence detector. It can detect the presence of a user and AccessAgent can be configured to perform specific actions. In previous releases, it is called Active Proximity Badge. 

**ActiveCode.** Short-lived authentication codes that are generated and verified by IBM Security Access Manager for Enterprise Single Sign-On. There are two types of ActiveCodes: Mobile ActiveCodes and Predictive ActiveCodes. 

Mobile ActiveCodes are generated by IBM Security Access Manager for Enterprise Single Sign-On and dispatched to the mobile phone or email account of the user. Predictive ActiveCodes, or One Time Passwords, are generated from OTP tokens when a user presses its button. 

Combined with alternative channels or devices, ActiveCodes provide effective second-factor authentication. 

**Administrator.** A person responsible for administrative tasks such as access authorization and content management. Administrators can also grant levels of authority to users. 

**Application policies.** A collection of policies and attributes governing access to applications. 

**Application programming interface (API).** An interface that allows an application program written in a high-level language to use specific data or functions of the operating system or another program. 

**Application.** One or more computer programs or software components that provide a function in direct support of a specific business process or processes. In AccessStudio, it is the system that provides the user interface for reading or entering the authentication credentials. 

**Audit.** A process that logs the user, Administrator, and Helpdesk activities. 

**Authentication factor.** The different devices, biometrics, or secrets required as credentials for validating digital identities. Examples of authentication 

**59** 

© Copyright IBM Corp. 2002, 2012 

factors are passwords, smart card, RFID, biometrics, and one-time password tokens. 

**Authentication service.** In IBM Security Access Manager for Enterprise Single Sign-On, a service that verifies the validity of an account against their own user store or against a corporate directory. Identifies the authentication service associated with a screen. Account data saved under a particular authentication service is retrieved and auto-filled for the logon screen that is defined. Account data captured from the logon screen defined is saved under this authentication service. 

**Authorization code.** An alphanumeric code generated for administrative functions, such as password resets or two-factor authentication bypass with AccessAgent, AccessAssistant, and Web Workplace. 

**Auto-capture.** A process that allows a system to collect and reuse user credentials for different applications. These credentials are captured when the user enters information for the first time, and then stored and secured for future use. 

**Automatic sign-on.** A feature where users can log on to the sign-on automation system and the system logs on the user to all other applications. 

**Base distinguished name.** A name that indicates the starting point for searches in the directory server. 

**Bidirectional language.** A language that uses a script, such as Arabic and Hebrew, whose general flow of text proceeds horizontally from right to left, but numbers, English, and other left-to-right language text are written from left to right. 

**Bind distinguished name.** A name that specifies the credentials for the application server to use when connecting to a directory service. The distinguished name uniquely identifies an entry in a directory. See also _Distinguished name_ . 

**Biometrics.** The identification of a user based on a physical characteristic of the user, such as a fingerprint, iris, face, voice, or handwriting. 

**Card Serial Number (CSN).** A unique data item that identifies a hybrid smart card. It has no relation to the certificates installed in the smart card 

**Cell.** In WebSphere Application Server, a cell is a virtual unit that consists of a deployment manager and one or more nodes. 

**Certificate authority (CA).** A trusted organization or company that issues the digital certificates. The certificate authority typically verifies the identity of the individuals who are granted the unique certificate. 

**IMS Server Certificate.** Used in IBM Security Access Manager for Enterprise Single Sign-On. The IMS Server Certificate allows clients to identify and authenticate an IMS Server. 

**Client AccessAgent.** AccessAgent installed and running on the client machine. 

**Client workstation, client machine, client computers.** Computers where AccessAgent installed. 

**Clinical Context Object Workgroup (CCOW).** A vendor independent standard, for the interchange of information between clinical applications in the healthcare industry. 

**Clustering.** In WebSphere Application Server, clustering is the ability to group application servers. 

**Clusters.** A group of application servers that collaborate for the purposes of workload balancing and failover. 

**Command line interface.** A computer interface in which the input command is a string of text characters. 

**Credentials.** Information acquired during authentication that describes a user, group associations, or other security-related identity attributes, and that is used to perform services such as authorization, auditing, or delegation. For example, a user ID and password are credentials that allow access to network and system resources. 

**Cryptographic application programming interface (CAPI).** An application programming interface that provides services to enable developers to secure applications using cryptography. It is a set of dynamically-linked libraries that provides an abstraction layer which isolates programmers from the code used to encrypt the data. 

**Cryptographic Service Provider (CSP).** A feature of the i5/OS[®] operating system that provides APIs. The CCA Cryptographic Service Provider enables a user to run functions on the 4758 Coprocessor. 

**Data source.** The means by which an application accesses data from a database. 

**Database (DB) server.** A software program that uses a database manager to provide database services to software programs or computers. 

**DB2[®] .** A family of IBM licensed programs for relational database management. 

**Deployment manager profiles.** A WebSphere Application Server runtime environment that manages operations for a logical group, or cell, of other servers. 

**Deployment manager.** A server that manages and configures operations for a logical group or cell of other servers. 

**60** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

**Deprovision.** To remove a service or component. For example, to deprovision an account means to delete an account from a resource. 

**Desktop application.** Application that runs in a desktop. 

**Desktop Manager.** Manages concurrent user desktops on a single workstation 

**Direct auth-info.** In profiling, direct auth-info is a direct reference to an existing authentication service. 

**Directory service.** A directory of names, profile information, and computer addresses of every user and resource on the network. It manages user accounts and network permissions. When a user name is sent, it returns the attributes of that individual, which might include a telephone number, or an email address. Directory services use highly specialized databases that are typically hierarchical in design and provide fast lookups. 

**Directory.** A file that contains the names and controlling information for objects or other directories. 

**Disaster recovery site.** A secondary location for the production environment in case of a disaster. 

**Disaster recovery.** The process of restoring a database, system, policies after a partial or complete site failure that was caused by a catastrophic event such as an earthquake or fire. Typically, disaster recovery requires a full backup at another location. 

**Distinguished name.** The name that uniquely identifies an entry in a directory. A distinguished name is made up of attribute:value pairs, separated by commas. For example, CN=person name and C=country or region. 

**Distributed IMS Server.** The IMS Servers are deployed in multiple geographical locations. 

**Domain name server (DNS).** A server program that supplies name-to-address conversion by mapping domain names to IP addresses. 

**Dynamic link library (DLL).** A file containing executable code and data bound to a program at load time or run time, rather than during linking. The code and data in a DLL can be shared by several applications simultaneously. 

**Enterprise directory.** A directory of user accounts that define IBM Security Access Manager for Enterprise Single Sign-On users. It validates user credentials during sign-up and logon, if the password is synchronized with the enterprise directory password. An example of an enterprise directory is Active Directory. 

**Enterprise Single Sign-On (ESSO).** A mechanism that allows users to log on to all applications deployed in the enterprise by entering a user ID and other credentials, such as a password. 

**Enterprise user name.** The user name of a user account in the enterprise directory. 

**ESSO audit logs.** A log file that contains a record of system events and responses. ESSO audit logs are stored in the IMS Database. 

**ESSO Credential Provider.** Previously known as the Encentuate Credential Provider (EnCredentialProvider), this is the IBM Security Access Manager for Enterprise Single Sign-On GINA for Windows Vista and Windows 7. 

**ESSO credentials.** The ISAM ESSO user name and password. 

**ESSO GINA.** Previously known as the Encentuate GINA (EnGINA). IBM Security Access Manager for Enterprise Single Sign-On GINA provides a user interface that is integrated with authentication factors and provide password resets and second factor bypass options. 

**ESSO Network Provider.** Previously known as the Encentuate Network Provider (EnNetworkProvider). An AccessAgent module that captures the Active Directory server credentials and uses these credentials to automatically log on the users to their Wallet. 

**ESSO password.** The password that secures access to the user Wallet. 

**Event code.** A code that represents a specific event that is tracked and logged into the audit log tables. 

**Failover.** An automatic operation that switches to a redundant or standby system in the event of a software, hardware, or network interruption. 

**Fast user switching.** A feature that allows users to switch between user accounts on a single workstation without quitting and logging out of applications. 

**Federal Information Processing Standard (FIPS).** A standard produced by the National Institute of Standards and Technology when national and international standards are nonexistent or inadequate to satisfy the U.S. government requirements. 

**Fix pack.** A cumulative collection of fixes that is made available between scheduled refresh packs, manufacturing refreshes, or releases. It is intended to allow customers to move to a specific maintenance level. 

**Fully qualified domain name (FQDN).** In Internet communications, the name of a host system that 

Glossary **61** 

includes all of the subnames of the domain name. An example of a fully qualified domain name is rchland.vnet.ibm.com. 

**Graphical Identification and Authentication (GINA).** A dynamic link library that provides a user interface that is tightly integrated with authentication factors and provides password resets and second factor bypass options. 

**Group Policy Object (GPO).** A collection of group policy settings. Group policy objects are the documents created by the group policy snap-in. Group policy objects are stored at the domain level, and they affect users and computers contained in sites, domains, and organizational units. 

**High availability (HA).** The ability of IT services to withstand all outages and continue providing processing capability according to some predefined service level. Covered outages include both planned events, such as maintenance and backups, and unplanned events, such as software failures, hardware failures, power failures, and disasters. 

**Host name.** In Internet communication, the name given to a computer. The host name might be a fully qualified domain name such as mycomputer.city.company.com, or it might be a specific subname such as mycomputer. 

**Hot key.** A key sequence used to shift operations between different applications or between different functions of an application. 

**Hybrid smart card.** An ISO-7816 compliant smart card which contains a public key cryptography chip and an RFID chip. The cryptographic chip is accessible through contact interface. The RFID chip is accessible through contactless (RF) interface. 

**IBM HTTP server.** A web server. IBM offers a web server, called the IBM HTTP Server, that accepts requests from clients and forward to the application server. 

**IMS Bridge.** A module embedded in third-party applications and systems to call to IMS APIs for provisioning and other purposes. **IMS Configuration Utility.** A utility of the IMS Server that allows Administrators to manage lower-level configuration settings for the IMS Server. 

**IMS Configuration wizard.** Administrators use the wizard to configure the IMS Server during installation. 

**IMS Connector.** A module that connects IMS to external systems to dispatch a mobile active code to a messaging gateway. 

**IMS data source.** A WebSphere Application Server configuration object that defines the location and parameters for accessing the IMS database. 

**IMS Database.** The relational database where the IMS Server stores all ESSO system, machine, and user data and audit logs. 

**IMS Root CA.** The root certificate authority that signs certificates for securing traffic between AccessAgent and IMS Server. 

**IMS Server.** An integrated management system for ISAM ESSO that provides a central point of secure access administration for an enterprise. It enables centralized management of user identities, AccessProfiles, authentication policies, provides loss management, certificate management, and audit management for the enterprise. 

**Indirect auth-info.** In profiling, indirect auth-info is an indirect reference to an existing authentication service. 

**Interactive graphical mode.** A series of panels that prompts for information to complete the installation. 

**IP address.** A unique address for a device or logical unit on a network that uses the Internet Protocol standard. 

**Java Management Extensions (JMX).** A means of doing management of and through Java technology. JMX is a universal, open extension of the Java programming language for management that can be deployed across all industries, wherever management is needed. 

**Java runtime environment (JRE).** A subset of a Java developer kit that contains the core executable programs and files that constitute the standard Java platform. The JRE includes the Java virtual machine (JVM), core classes, and supporting files. 

**Java virtual machine (JVM).** A software implementation of a processor that runs compiled Java code (applets and applications). 

**Keystore.** In security, a file or a hardware cryptographic card where identities and private keys are stored, for authentication and encryption purposes. Some keystores also contain trusted, or public, keys. 

**Lightweight Directory Access Protocol (LDAP).** An open protocol that uses TCP/IP to provide access to directories that support an X.500 model. An LDAP can be used to locate people, organizations, and other resources in an Internet or intranet directory. 

**Lightweight mode.** A Server AccessAgent mode. Running in lightweight mode reduces the memory footprint of AccessAgent on a Citrix/Terminal Server and improves the single sign-on startup duration. 

**62** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

**Load balancing.** The monitoring of application servers and management of the workload on servers. If one server exceeds its workload, requests are forwarded to another server with more capacity. 

**Lookup user.** A user who is authenticated in the Enterprise Directory and searches for other users. IBM Security Access Manager for Enterprise Single Sign-On uses the lookup user to retrieve user attributes from the Active Directory or LDAP enterprise repository. 

**Main AccessProfile.** The AccessProfile that contains one or more AccessProfile widgets 

**Managed node.** A node that is federated to a deployment manager and contains a node agent and can contain managed servers. 

**Microsoft Cryptographic application programming interface (CAPI).** An interface specification from Microsoft for modules that provide cryptographic functionality and that allow access to smart cards. 

**Mobile ActiveCode (MAC).** A one-time password that is used by users for two-factor authentication in Web Workplace, AccessAssistant, and other applications. This OTP is randomly generated and dispatched to user through SMS or email. 

**Mobile authentication.** An authentication factor which allows mobile users to sign-on securely to corporate resources from anywhere on the network. 

**Network deployment.** Also known as a clustered deployment. A type of deployment where the IMS Server is deployed on a WebSphere Application Server cluster. 

**Node agent.** An administrative agent that manages all application servers on a node and represents the node in the management cell. 

**Nodes.** A logical group of managed servers. 

**One-Time Password (OTP).** A one-use password generated for an authentication event, sometimes communicated between the client and the server through a secure channel. 

**OTP token.** A small, highly portable hardware device that the owner carries to authorize access to digital systems and physical assets. 

**Password aging.** A security feature by which the superuser can specify how often users must change their passwords. 

**Password complexity policy.** A policy that specifies the minimum and maximum length of the password, the minimum number of numeric and alphabetic characters, and whether to allow mixed uppercase and lowercase characters. 

**Personal applications.** Windows and web-based applications where AccessAgent can store and enter credentials. 

Some examples of personal applications are web-based mail sites such as Company Mail, Internet banking sites, online shopping sites, chat, or instant messaging programs. 

**Personal desktop.** The desktop is not shared with any other users. 

**Personal Identification Number (PIN).** In Cryptographic Support, a unique number assigned by an organization to an individual and used as proof of identity. PINs are commonly assigned by financial institutions to their customers. 

**Pinnable state.** A state from the AccessProfile widget that is declared as 'Can be pinned in another AccessProfile'. 

**Pinned state.** A pinnable state that is attached to a state in the main AccessProfile. 

**Policy template.** A predefined policy form that helps users define a policy by providing the fixed policy elements that cannot be changed and the variable policy elements that can be changed. 

**Portal.** A single, secure point of access to diverse information, applications, and people that can be customized and personalized. 

**Presence detector.** A device that, when fixed to a computer, detects when a person moves away from it. This device eliminates manually locking the computer upon leaving it for a short time. 

**Primary authentication factor.** The IBM Security Access Manager for Enterprise Single Sign-On password or directory server credentials. 

**Private desktop.** Under this desktop scheme, users have their own Windows desktops in a workstation. When a previous user return to the workstation and unlocks it, AccessAgent switches to the desktop session of the previous user and resumes the last task. 

**Private key.** In computer security, the secret half of a cryptographic key pair that is used with a public key algorithm. The private key is known only to its owner. Private keys are typically used to digitally sign data and to decrypt data that has been encrypted with the corresponding public key. 

**Provisioning API.** An interface that allows IBM Security Access Manager for Enterprise Single Sign-On to integrate with user provisioning systems. 

**Provisioning bridge.** An automatic IMS Server credential distribution process with third party provisioning systems that uses API libraries with a SOAP connection. 

Glossary **63** 

**Provisioning system.** A system that provides identity lifecycle management for application users in enterprises and manages their credentials. 

**Provision.** To provide, deploy, and track a service, component, application, or resource. 

**Public Key Cryptography Standards.** A set of industry-standard protocols used for secure information exchange on the Internet. Domino[®] Certificate Authority and Server Certificate Administration applications can accept certificates in PKCS format. 

**Published application.** Application installed on Citrix XenApp server that can be accessed from Citrix ICA Clients. 

**Published desktop.** A Citrix XenApp feature where users have remote access to a full Windows desktop from any device, anywhere, at any time. **Radio Frequency Identification (RFID).** An automatic identification and data capture technology that identifies unique items and transmits data using radio waves. 

**Random password.** An arbitrarily generated password used to increase authentication security between clients and servers. 

**Registry hive.** In Windows systems, the structure of the data stored in the registry. 

**Registry.** A repository that contains access and configuration information for users, systems, and software. 

**Secret question.** A question whose answer is known only to the user. A secret question is used as a security feature to verify the identity of a user. 

**Secure Remote Access.** The solution that provides web browser-based single sign-on to all applications from outside the firewall. 

**Secure Sockets Layer (SSL).** A security protocol that provides communication privacy. With SSL, client/server applications can communicate in a way that is designed to prevent eavesdropping, tampering, and message forgery. 

**Secure Sockets Layer virtual private network (SSL VPN).** A form of VPN that can be used with a standard web browser. 

**Security Token Service (STS).** A web service used for issuing and exchanging of security tokens. 

**Security trust service chain.** A group of module instances that are configured for use together. Each module instance in the chain is called in turn to perform a specific function as part of the overall processing of a request. 

**Self-service features.** Features in IBM Security Access Manager for Enterprise Single Sign-On which users can use to perform basic tasks such as resetting passwords and secrets with minimal assistance from Help desk or your Administrator. 

**Serial ID Service Provider Interface (SPI).** A programmatic interface intended for integrating AccessAgent with third-party Serial ID devices used for two-factor authentication. 

## **Remote Authentication Dial-In User Service** 

**(RADIUS).** An authentication and accounting system that uses access servers to provide centralized management of access to large networks. 

**Remote Desktop Protocol (RDP).** A protocol that facilitates remote display and input over network connections for Windows-based server applications. RDP supports different network topologies and multiple connections. 

**Replication.** The process of maintaining a defined set of data in more than one location. Replication involves copying designated changes for one location (a source) to another (a target) and synchronizing the data in both locations. 

**Revoke.** To remove a privilege or an authority from an authorization identifier. **Root certificate authority (CA).** The certificate authority at the top of the hierarchy of authorities by which the identity of a certificate holder can be verified. 

**Scope.** A reference to the applicability of a policy, at the system, user, or machine level. 

**Serial number.** A unique number embedded in the IBM Security Access Manager for Enterprise Single Sign-On Keys, which is unique to each Key and cannot be changed. 

**Server AccessAgent.** AccessAgent deployed on a Microsoft Windows Terminal Server or a Citrix server. 

**Server locator.** A locator that groups a related set of web applications that require authentication by the same authentication service. In AccessStudio, server locators identify the authentication service with which an application screen is associated. **Service Provider Interface (SPI).** An interface through which vendors can integrate any device with serial numbers with IBM Security Access Manager for Enterprise Single Sign-On and use it as a second factor in AccessAgent. 

**Session management.** Management of user session on private desktops and shared desktops. 

**Shared desktop.** A desktop configuration where multiple users share a generic Windows desktop. 

**64** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

**Shared workstation.** A workstation shared among users. 

**Sign up.** To request a resource. **sign-on automation.** A technology that works with application user interfaces to automate the sign-on process for users. 

**sign-on information.** Information required to provide access to users to any secure application. This information can include user names, passwords, domain information, and certificates. 

**Signature.** In profiling, unique identification information for any application, window, or field. 

**Silent mode.** A method for installing or uninstalling a product component from the command line with no GUI display. When using silent mode, you specify the data required by the installation or uninstallation program directly on the command line or in a file (called an option file or response file). 

**Simple Mail Transfer Protocol (SMTP).** An Internet application protocol for transferring mail among users of the Internet. 

**Simple Object Access Protocol (SOAP).** A lightweight, XML-based protocol for exchanging information in a decentralized, distributed environment. SOAP can be used to query and return information and invoke services across the Internet. 

**Single sign-on.** An authentication process in which a user can access more than one system or application by entering a single user ID and password. 

**Smart card middleware.** Software that acts as an interface between smart card applications and the smart card hardware. Typically the software consists of libraries that implement PKCS#11 and CAPI interfaces to smart cards. 

**Smart card.** An intelligent token that is embedded with an integrated circuit chip that provides memory capacity and computational capabilities. 

**Stand-alone deployment.** A deployment where the IMS Server is deployed on an independent WebSphere Application Server profile. 

**Stand-alone server.** A fully operational server that is managed independently of all other servers, and it uses its own administrative console. 

**Strong authentication.** A solution that uses multi-factor authentication devices to prevent unauthorized access to confidential corporate information and IT networks, both inside and outside the corporate perimeter. 

**Strong digital identity.** An online persona that is difficult to impersonate, possibly secured by private keys on a smart card. 

**System modal message.** A system dialog box that is typically used to display important messages. When a system modal message is displayed, nothing else can be selected on the screen until the message is closed. 

**Terminal emulator.** A program that allows a device such as a microcomputer or personal computer to enter and receive data from a computer system as if it were a particular type of attached terminal 

**Thin client.** A client machine that has little or no installed software. It has access to applications and desktop sessions that is running on network servers that are connected to it. A thin client machine is an alternative to a full-function client such as a workstation. 

**Tivoli Common Reporting tool.** A reporting component that you can use to create, customize, and manage reports. 

**Tivoli Identity Manager adapter.** An intermediary software component that allows IBM Security Access Manager for Enterprise Single Sign-On to communicate with Tivoli Identity Manager. 

**Transparent screen lock.** A feature that, when enabled, permits users to lock their desktop screens but still see the contents of their desktop. 

**Trigger.** In profiling, an event that causes transitions between states in a states engine, such as, the loading of a web page or the appearance of window on the desktop. 

**Trust service chain.** A chain of modules operating in different modes. For example: validate, map and issue. 

**Truststore.** In security, a storage object, either a file or a hardware cryptographic card, where public keys are stored in the form of trusted certificates, for authentication purposes in web transactions. In some applications, these trusted certificates are moved into the application keystore to be stored with the private keys. 

**TTY (terminal type).** A generic device driver for a text display. A tty typically performs input and output on a character-by-character basis. 

**Two-factor authentication.** The use of two factors to authenticate a user. For example, the use of password and an RFID card to log on to AccessAgent. 

**Uniform resource identifier.** A compact string of characters for identifying an abstract or physical resource. 

Glossary **65** 

**User credential.** Information acquired during authentication that describes a user, group associations, or other security-related identity attributes, and that is used to perform services such as authorization, auditing, or delegation. For example, a user ID and password are credentials that allow access to network and system resources. 

**User deprovisioning.** Removing the user account from IBM Security Access Manager for Enterprise Single Sign-On. 

**User provisioning.** The process of signing up a user to use IBM Security Access Manager for Enterprise Single Sign-On. 

**Virtual appliance.** A virtual machine image with a specific application purpose that is deployed to virtualization platforms. 

**Virtual channel connector.** A connector that is used in a terminal services environment. The virtual channel connector establishes a virtual communication channel to manage the remote sessions between the Client AccessAgent component and the Server AccessAgent. 

**Virtual Member Manager (VMM).** A WebSphere Application Server component that provides applications with a secure facility to access basic organizational entity data such as people, logon accounts, and security roles. 

**Virtual Private Network (VPN).** An extension of a company intranet over the existing framework of either a public or private network. A VPN ensures that the data that is sent between the two endpoints of its connection remains secure. 

**Visual Basic (VB).** An event-driven programming language and integrated development environment (IDE) from Microsoft. 

**Wallet caching.** When performing single sign-on for an application, AccessAgent retrieves the logon credentials from the user credential Wallet. The user credential Wallet is downloaded on the user machine and stored securely on the IMS Server. So users can access their Wallet even when they log on to IBM Security Access Manager for Enterprise Single Sign-On from a different machine later. 

**Web server.** A software program that is capable of servicing Hypertext Transfer Protocol (HTTP) requests. 

**Web service.** A self-contained, self-describing modular application that can be published, discovered, and invoked over a network using standard network protocols. Typically, XML is used to tag the data, SOAP is used to transfer the data, WSDL is used for describing the services available, and UDDI is used for listing what services are available. 

**Web Workplace.** A web-based interface that users can log on to enterprise web applications by clicking links without entering the passwords for individual applications. This interface can be integrated with the existing portal or SSL VPN of the customer. **WebSphere Administrative console.** A graphical administrative Java application client that makes method calls to resource beans in the administrative server to access or modify a resource within the domain. 

**WebSphere Application Server profile.** The WebSphere Application Server administrator user name and profile. Defines the runtime environment. 

**WebSphere Application Server.** Software that runs on a web server and that can deploy, integrate, execute, and manage e-business applications. 

**Windows logon screen, Windows logon UI mode.** The screen where users enter their user name and password to log on to the Windows desktop. 

**Windows native fast user switching.** A Windows XP feature which allows users to quickly switch between user accounts. 

**Windows Terminal Services.** A Microsoft Windows component that users use to access applications and data on a remote computer over a network. 

**WS-Trust.** A web services security specification that defines a framework for trust models to establish trust between web services. 

**Wallet manager.** The IBM Security Access Manager for Enterprise Single Sign-On GUI component that users can use to manage application credentials in the personal identity Wallet. 

**Wallet Password.** A password that secures access to the Wallet. 

**Wallet.** A secured data store of access credentials of a user and related information, which includes user IDs, passwords, certificates, encryption keys. 

**66** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## **Index** 

## **A** 

abends 8 AccessAdmin 

Back button not working 30 cluster hostname not working 20 troubleshooting 20, 30 AccessAgent AccessAgent installation file is corrupt 11 application conflicts 14 console application support disabled 26 IMS Server cannot be found 13 IMS Server certificate download 13 installed before Mozilla Firefox 29 module registration 14 Mozilla Firefox single sign-on feature 29 troubleshooting 13, 14, 18, 27, 29 AccessAssistant and Web Workplace Back button not working 30 troubleshooting 30 accessibility viii Active Proximity Badges registration problems 14 unlock computer 15 Active RFID cards logging on to Wallet 15 activity.log 40, 43 analyzing log data 37 APAR 35 authentication factor lost 16 

## **B** 

books _See_ publications 

## **C** 

certificates not issued for an application 25 checklist for troubleshooting 1, 9 collecting data for a problem 39 connectivity troubleshooting 5 connectivity problems overview 5 contacting IBM Software Support 49 contracts, software maintenance 50 conventions typeface ix crashes 8 

## **D** 

data, collecting for a problem 39 directory names, notation ix 

## **E** 

## **M** 

EcuRep service 52 maintenance contracts 50 education manuals 

_See_ Tivoli technical training Electronic Service Request 52 environment variables, notation ix error messages 7 ESR tool 52 

_See_ publications message logs 40 messages 7 methods for submitting data to IBM 51 

## **N** 

## **F** 

notation environment variables ix path names ix typeface ix 

file names of message logs 41 file names of trace logs 42 fix notifications, setup 33 fix pack 6 fixes to product 6 fixes, obtaining 33 FTP EcuRep service 52 

## **O** 

online publications accessing vii ordering publications vii 

## **I** 

IBM Service log path 41 steps to configure 43 IBM Support Assistant 39, 49, 51 IMS Server 

## **P** 

password problems 17 path names, notation ix performance problems 7 problem-specific data 39 problems 

troubleshooting 20, 25, 27 Internet explorer problems 30 Internet, searching to find software problem resolution 33 

collecting data 39 obtaining symptoms 3 performance 7 report 51 product education 5 product fixes 6 publications v accessing online vii ordering vii 

## **J** 

JVM log filepath 41 steps to configure 42 

## **K** 

## **R** 

knowledge bases, searching 35 

refresh pack 6 

## **L** 

## **S** 

logon credentials 30 logs analyzing data 37 enabling trace at server startup 43 enabling trace on a running server 44 file names 40, 41 locations 41, 42 message 41 message types 40 trace 41, 42 viewing 45 

severity levels of problems 51 software maintenance contracts 50 software support, contacting 49 submitting data to IBM, methods 51 SystemOut.log 40 

## **T** 

technotes 35 Tivoli Information Center vii Tivoli technical training viii Tivoli user groups viii trace logs 41 trace.log 41 

**67** 

© Copyright IBM Corp. 2002, 2012 

training, Tivoli technical viii traps 8 troubleshooting checklist 1, 9 obtaining symptoms 3 process 1 typeface conventions ix types of messages 40 

## **U** 

updates to product 6 user groups, Tivoli viii 

## **V** 

variables, notation for ix viewing logs 45 

## **W** 

Wallet-related problems 18 Web site for fixes 6 

**68** IBM[®] Security Access Manager for Enterprise Single Sign-On: Troubleshooting and Support Guide 

## ���� 

Printed in USA 

GC23-9693-01 

**==> picture [188 x 37] intentionally omitted <==**