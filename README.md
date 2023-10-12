# Start2Impact Blockchain Final Project

<p align="center">
    <img src="images/Logo.png" alt="BlockSneakers logo">
</p>

This is my Blockchain Final project for [Start2Impact](https://talent.start2impact.it/profile/riccardo-santi).

### The main purpose of this project is to build an auction platform to sell limited edition shoes for an eco-friendly footwear company using Django, Redis and Web3PY.

BlockSneakers is an auction platform designed to sell limited edition shoes for an eco-friendly footwear company.
The platform allows users to register and log into the platform and gives a welcome bonus of 5000€ to every new user to start making bids. 
Customers can place bids on open auctions and easily monitor their wallet balance and won auctions.
When an auction concludes, BlockSneakers sends an Ethereum Sepolia transaction containg the sha256 hash of the auction JSON report.
BlockSneakers embraces transparent auctions, empowering users to independently verify results using the secure and immutable blockchain technology.


__Django__ is a powerful and popular Python based web framework for building web applications.
<br>
__Redis__ is an in-memory NoSQL database used for fast data storage and retrieval.
<br>
__Web3PY__ is a Python library that provides developers easy interaction with Ethereum blockchain.

<hr/>


## 📖Index

- [ 🚀 Main Features ](#mainfeatures)
- [ 🛠️ How to deploy ](#howtodeploy)
- [ 📈 Improved Skills ](#improvedskills)
- [ 👨‍💻 About me ](#aboutme)



<a name="mainfeatures"></a>
## 🚀 Main Features: 


- #### A website homepage with a brief explanation of BlockSneakers
<p align="center">
    <img src="images/1.png" alt="HOMEPAGE - IMAGE 1">
</p>
<br><br>


- #### A section where users can create a new account and log into the platform
<p align="center">
    <img src="images/2.png" alt="REGISTER - IMAGE 2">
    <img src="images/3.png" alt="LOGIN - IMAGE 3">
    <img src="images/4.png" alt="PROFILE - IMAGE 4">
</p>
<br><br>


- #### A dashboard page where users can see their wallet balance, their total bids and their total auctions won
<p align="center">
    <img src="images/5.png" alt="USER DROPDOWN - IMAGE 5">
    <img src="images/6.png" alt="DASHBOARD - IMAGE 6">
</p>
<br><br>


- #### A page where anyone can see the list of open auctions 
<p align="center">
    <img src="images/7.png" alt="OPEN AUCTIONS 1 - IMAGE 7">
    <img src="images/8.png" alt="OPEN AUCTIONS 2 - IMAGE 8">
</p>
<br><br>


- #### A page where customers can make bids on open auctions
<p align="center">
    <img src="images/9.png" alt="NEW BID - IMAGE 9">
</p>
<br><br>


- #### A page where users can see their bids made
<p align="center">
    <img src="images/10.png" alt="OPEN AUCTIONS UPDATE - IMAGE 10">
    <img src="images/11.png" alt="DASHBOARD UPDATE - IMAGE 11">
    <img src="images/12.png" alt="USER BIDS - IMAGE 12">
</p>
<br><br>


- #### A page where anyone can see the list of closed auctions, with on-chain proof
<p align="center">
    <img src="images/13.png" alt="CLOSED AUCTIONS - IMAGE 13">
    <img src="images/14.png" alt="AUCTION ONCHAIN PROOF - IMAGE 14">
</p>
<br><br>


- #### A page where users can see their auctions won, with on-chain proof
<p align="center">
    <img src="images/15.png" alt="AUCTIONS WON - IMAGE 15">
</p>
<br><br>


- #### The ability to adapt the website page and content to different types of devices to allow users to have always the best experience
<p align="center">
    <img src="images/16.png" alt="WEBSITE ADAPTATION EXAMPLE - IMAGE 16">
</p>
<br><br>



<a name="howtodeploy"></a>
## 🛠️ How to deploy

- Clone this repository in your local
- Be sure to have Python installed on your device, for this project i used Python 3.10.9.
- Be sure to have a Python IDE on board (I recommend [PyCharm](https://www.jetbrains.com/pycharm/))
- Open the program main directory in your IDE, open new terminal window and type `pip install virtualenv`
- Create a virtual environment by typing `python3.10  -m venv env` and activate it with `source env/bin/activate`
- Install program requirements by typing `pip install -r requirements.txt`
- Initialize the program database by typing `cd project`, `python3 manage.py makemigrations` and `python3 manage.py migrate`
- Create an admin user to start new auctions `python3 manage.py createsuperuser`
- Run the program by typing `python3 manage.py runserver`
- Enjoy BlockSneakers!


<a name="improvedskills"></a>
## 📈 Improved Skills
Python, [Django](https://www.djangoproject.com/), [Redis](https://redis.io/), [Web3PY](https://web3py.readthedocs.io/en/stable/), HTML & CSS


<a name="aboutme"></a>
## 👨‍💻 About me
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/riccardo-santi/) &nbsp;&nbsp;
[![website](https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://riccardo-santi.vercel.app/)

