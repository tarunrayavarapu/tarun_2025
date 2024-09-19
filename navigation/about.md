---
layout: page
title: About
permalink: /about/
hide_title: true
---

{%include nav/home.html %}

<script src="https://utteranc.es/client.js"
        repo="tarunrayavarapu/tarun_2025"
        issue-term="title"
        label="blogpost-comment"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>

<h1>About<h1>
<h1>AP Computer Science Principles</h1>

**Tarun Rayavarapu**

**Period 2**


<h2>About Me/Why I Took This Class:</h2>


  <li style="margin-bottom: 10px;">I took this class because both of my parents are software engineers</li>
  <li style="margin-bottom: 10px;">Coding is the future of our world</li>
  <li style="margin-bottom: 10px;">This class would improve my coding skills</li>
  <li style="margin-bottom: 10px;">CS is important for many careers</li>
  <li style="margin-bottom: 10px;">Challenging myself with this class is good for me</li>
  
  <div style="flex: 1; text-align: center;">
    <img src="https://media.licdn.com/dms/image/D5612AQEdsqnka0y4Ng/article-cover_image-shrink_720_1280/0/1709474763485?e=2147483647&v=beta&t=yaDe74OO54QD-7b9OPtUjhSDK3AKN-1wy7UlGCMfSNQ" alt="Image 1" style="max-width: 25%; height: auto; margin-bottom: 20px;">
    <img src="https://i.pinimg.com/originals/9e/43/44/9e4344fbf8840d797623bdaedae115e8.png" alt="Image 2" style="max-width: 25%; height: auto;">
  </div>


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