# Ex04 Places Around Me
# Date:01.12.2025
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using <map> tag name the map.

## STEP 4
Create clickable regions in the image using <area> tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
```
views.py:

from django.shortcuts import render
def maps(request):
    return render(request,'image.html')
def sar(request):
    return render(request,'saravana.html')
def grtjewel(request):
    return render(request,'grt.html')
def geet(request):
    return render(request,'geetham.html')
def bat(request):
    return render(request,'bata.html')
```
```
urls.py:

from django.contrib import admin
from django.urls import path
from exp4 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.maps),
    path('sar/',views.sar,name="saravana"),
    path('grt/',views.grtjewel,name="grt"),
    path('geet/',views.geet,name="geetham"),
    path('bata/',views.bat,name="bata"),
]
```
```
css.css:
 img {
     margin-left: auto;
     margin-right: auto;
     display: block;
     width: auto;
     height: 50%;
     border-radius: 15px;
 }

 p {
     text-align: justify;
     font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
     margin-left: 70px;
     margin-right: 70px;
     margin-top: 37px;
     font-size: 24px;
     line-height: 36px;
 }

 h1 {
     text-align: center;
     font-size: 37px;
     padding: 1%;
     font-family: Georgia, 'Times New Roman', Times, serif;
 }
```
```
saravana.html:

{% load static %}
<html>

<head>
    <title>SARAVANA STORES</title>
    <link rel="stylesheet" href="{% static 'css.css' %}">
</head>

<body style="background:linear-gradient(180deg,#307b8e,#a9d3c5,#d5e9e2);">
    <h1 style="color:whitesmoke;">The Legend Saravana Stores</h1>
    <img src="{% static 'Saravana.jpg' %}">
    <p style="color:#0b0829">
        Saravana Stores in T. Nagar is one of Chennai’s most popular and bustling retail
        landmarks, attracting thousands of shoppers every day. Known for its huge multi-floor
        layout, the store offers an unbeatable range of products—from clothing, sarees,
        jewelry, and accessories to home appliances, kitchenware, furniture, and electronics.
        Its biggest specialty is the combination of affordable pricing, endless variety,
        and a true “one-stop shopping” experience. Whether customers are looking for everyday
        essentials or festive purchases, Saravana Stores T. Nagar stands out for its value
        deals, wide product choices, and lively, fast-paced atmosphere that has become a
        trademark of the brand.
    </p>
</body>

</html>
```
```
grt.html:

{% load static %}
<html>

<head>
    <title>GRT</title>
    <link rel="stylesheet" href="{% static 'css.css' %}">
</head>

<body style="background:linear-gradient(180deg,#f2b635,blanchedalmond);">
    <h1 style="color:white;">GRT Jewellers</h1>
    <img src="{% static 'grt.jpg' %}">
    <p style="color:#0b0829">
        GRT Jewellers in T. Nagar is a landmark destination, representing a golden legacy of trust and craftsmanship since 1964. The multi-storey showroom is celebrated for its vast, exquisite collections that perfectly balance timeless traditional designs, especially in gold, with contemporary, lightweight styles across Gold, Certified Diamond, Platinum, and Silver jewellery. A specialty of this flagship store is its commitment to certified purity (BIS Hallmark) and providing an extensive selection for every life event, from daily wear to grand bridal occasions, cementing its reputation as one of South India's most respected jewellery houses.
    </p>
</body>

</html>
```
```
geetham.html:

{% load static %}
<html>

<head>
    <title>GEETHAM</title>
    <link rel="stylesheet" href="{% static 'css.css' %}">
</head>

<body style="background:linear-gradient(180deg,#f2b157,#e69951,#b5443b);">
    <h1 style="color:#dc2f02;">Geetham Veg Restaurant</h1>
    <img src="{% static 'Geetham.webp' %}" style="width: 43%;">
    <p style="color: rgb(237, 235, 235);">
        Geetham Veg Restaurant in T. Nagar is a popular pure vegetarian dining spot,
        renowned for its extensive multi-cuisine menu that features authentic South Indian staples, hearty North Indian dishes, and Indo-Chinese selections. A specialty of Geetham is its commitment to fresh, hygienic cooking and its ability to consistently deliver high-quality South Indian breakfast and tiffin items, such as the widely praised Ghee Roast and fragrant Filter Coffee, alongside a wide variety of juices and sweets. The location also often includes a Banquet Hall facility to host events, making it a versatile choice for both casual dining and special occasions.
    </p>
</body>

</html>
```
```
bata.html:

{% load static %}
<html>

<head>
    <title>BATA</title>
    <link rel="stylesheet" href="{% static 'css.css' %}">
</head>

<body style="background:linear-gradient(180deg,rgb(202, 11, 11),bisque);">
    <h1 style="color:bisque;">Bata Showroom</h1>
    <img src="{% static 'Bata.jpg' %}" style="width: 43%;">
    <p style="color:#b60005">
        The Bata showroom in T. Nagar is a go-to destination renowned for offering a comprehensive footwear solution for the entire family at affordable prices. Its specialty lies in its wide selection, which features the brand's trusted sub-labels like Hush Puppies (known for comfort and style), Power (for sports and fitness footwear), and Scholl (focusing on foot health). The store consistently stocks everything from durable school shoes and children's collections to elegant formal wear and the latest seasonal casual designs, making it a one-stop shop for reliable quality, exceptional comfort, and great value right in the heart of T. Nagar's bustling shopping district.
    </p>
</body>

</html>
```
# OUTPUT

![alt text](<gmaps/exp4/static/Screenshot 2025-12-01 235705.png>)

![alt text](<gmaps/exp4/static/Screenshot 2025-12-01 235754.png>)

![alt text](<gmaps/exp4/static/Screenshot 2025-12-01 235811.png>)

![alt text](<gmaps/exp4/static/Screenshot 2025-12-01 235826.png>)

![alt text](<gmaps/exp4/static/Screenshot 2025-12-01 235851.png>)

# RESULT
The program for implementing image maps using HTML is executed successfully.
