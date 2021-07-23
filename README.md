# Projet-CybersecuYnov

A projet in which we have to create a website with a vulnerability (SQL Injection).
We will explain how it works, how to exploit and how to fix it.

-sitevulnerable.py is the vulnerable one (obvious).
  When we analyze it, we can see a raw SQL request that can be used for a SQL injection. To avoid that, we can see in site.py that we used SQLAlchemy (an ORM (Object Relational Mapping)) to control our requests and the overall database. 
  The use of debug=true in app.run() is also hazardous while deploying the app. Using it during the development part of the projet is fine and strongly advised but DO NOT forget to remove at the end before releasing the app.
    
