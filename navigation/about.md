---
layout: page
title: About
permalink: /about/
hide_title: true
---

{%include nav/home.html %}

<h1>About<h1>
<h1>AP Computer Science Principles</h1>

**Tarun Rayavarapu**

**Period 2**


<h2>About Me/Why I Took This Class:</h2>


•My name is Tarun Rayavarapu and I am 15 years old
•I took this class because both of my parents are software engineers

•Coding is the future of our world

•This class would improve my coding skills

•Cs is important for many careers

•Challenging myself with this class is good for me

<td width = "200"><img src="{{site.baseurl}}/images/IMG_6721 (1).JPG" height="150" title="Me and Groupmates" alt=""></td>



<h2>What I Enjoy</h2>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Soccerball.svg/500px-Soccerball.svg.png" alt="Image 1" width="150">

<img src="https://static.vecteezy.com/system/resources/thumbnails/011/421/099/small/realistic-vector-basketball-isolated-png.png" alt="Image 2" width="150">

<img src="https://png.pngtree.com/png-clipart/20221001/ourmid/pngtree-fast-food-big-ham-burger-png-image_6244235.png" alt="Image 3" width="150">



<h2>My Background</h2>
Both my parents are from India, while most of my cousins live here in the USA. I've lived in California for my whole life.


<div class="flag-container">
    <div class="flag" id="californiaFlag">
        <p>California</p>
    </div>
    <div class="flag" id="indiaFlag">
        <p>India</p>
    </div>
</div>




<script>
     // JavaScript to dynamically insert image URLs
    var californiaFlagUrl = "https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_California.svg";
    var indiaFlagUrl = "https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg";




    document.getElementById('californiaFlag').innerHTML = '<img src="' + californiaFlagUrl + '" alt="California Flag"><p>California</p>';
    document.getElementById('indiaFlag').innerHTML = '<img src="' + indiaFlagUrl + '" alt="Indian Flag"><p>India</p>';