AnyMount
========

When people release code, they would also like to publish related resources (data/model) to make the code actually work. AnyMount is a toolkit to let users have fine-grained control of what resources to download on demand. 

Design
---------
At the core of AnyMount is a <b>key-value database</b> that maps a remote resource (such as namespaces at Dropbox) to a local directory. For example, we can link a Dropbox shared folder to some sub-directory in the codebase. 

```
https://www.dropbox.com/sh/47u1spt3cxj33zs/AABbw9B7tQevqWb14TQR939Pa?dl=0 
-> /test/model
```
Suppose the application is to release code. Two views of the databaes are maintained. 

<h3>Programmer View</h3>

Programmers can add key-value pairs to the database. AnyMount automatically takes care of how these resource options are presented to users, and how users could interact to mount the resources. 

<h3>User View</h3>

Users can see the list of resources available to mount under the directory, and their dependency relationships. 


Q & A
-----

<h3> Why not commit all resources to GitHub?</h3>

There are several reasons not to do so. 

First, usually data are massive entities. Commiting them to Github would dramatically reduce the download speed for code. 

Second, separating code and resources gives users the freedom to select the resources on demand. For example, if the code implements model A and B, and the user only wants to run A, then only data related to A needs to be downloaded.

And most importantly, some data are sensitive, which implies fine-grained access control. We need a delegate to take care of that smoothly.

License (GPL V3)
-----------------
Copyright (C) 2015 Tianlin Shi

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributeCd in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.


