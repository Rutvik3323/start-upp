from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json

with open("most-wickets-till-2022.json") as a:
    data1 = json.load(a)  # wickets
    with open("most-runs-till-2022.json") as b:
        data2 = json.load(b)  # runs
        with open("best-bowling-figs-till-2022.json") as c:
            data3 = json.load(c)  # bowling

app = FastAPI()


@app.get("/")
def my_main_page():
    my_homepage = """
    <!DOCTYPE html>
<html lang="en">
<head>
<title>Cricket Research Analysis</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body>

<!-- Header -->
<header class="w3-display-container w3-content w3-center" style="max-width:1500px">
  <style>
    nav {
  display: flex;
  justify-content: space-between;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

li:first-child {
  margin-left: 0;
}

li:last-child {
  margin-right: 0;
}

  </style>
  <nav>
  <ul>
    <li><a href="http://127.0.0.1:8000/">Home</a></li>
    <li><a href="http://127.0.0.1:8000/wicket">Highest Wickets</a></li>
    <li><a href="http://127.0.0.1:8000/video">Video</a></li>
    <li><a href="http://127.0.0.1:8000/pointstable">Points Table</a></li>
    <li><a href="http://127.0.0.1:8000/batsman">Batsman</a></li>
    <li><a href="http://127.0.0.1:8000/centuries">Centuries</a></li>
    <li><a href="http://127.0.0.1:8000/sponsors">Sponsors</a></li>
    <li><a href="http://127.0.0.1:8000/News">News</a></li>
    <li><a href="http://127.0.0.1:8000/about">About Us</a></li>
  </ul>
</nav>

  <div class="w3-display-Left w3-padding-large w3-border w3-wide w3-text-black w3-align:right">
    <h1 class="w3-hide-medium w3-hide-small w3-xxxlarge">CRA</h1>
    <h5 class="w3-hide-large" style="white-space:nowrap">JANE DOE</h5>
    <h3 class="w3-hide-medium w3-hide-small">Cricket Research Analysis</h3>
  </div>
  <img class="w3-image" src="https://i.pinimg.com/736x/85/b9/b4/85b9b4605207163aeacdaf78aa30ecb1.jpg" alt="Me" width="600" height="400">



  <!-- Navbar (placed at the bottom of the header image) -->
  <div class="w3-bar w3-light-grey w3-round w3-display-bottommiddle w3-hide-small" style="bottom:-16px">
    <a href="#" class="w3-bar-item w3-button">Home</a>
    <a href="#Teams" class="w3-bar-item w3-button">Teams</a>
    <a href="#contact" class="w3-bar-item w3-button">Contact</a>
  </div>
</header>

<!-- Navbar on small screens -->
<div class="w3-center w3-light-grey w3-padding-16 w3-hide-large w3-hide-medium">
<div class="w3-bar w3-light-grey">
  <a href="#" class="w3-bar-item w3-button">Home</a>
  <a href="#Teams" class="w3-bar-item w3-button">Teams</a>
  <a href="#contact" class="w3-bar-item w3-button">Contact</a>
</div>
</div>
<!-- Page content -->
<div class="w3-content w3-padding-large w3-margin-top" id="teams">


  <div class="image-row">
  <img src="https://i.pinimg.com/564x/93/44/80/9344800799339a47a254ad1f6c564c20.jpg" alt="Ocean" width="400" height="400">
  <img src="https://i.pinimg.com/236x/eb/ab/c9/ebabc996f7ef6dee11400acd443b156f.jpg" alt="Ocean II" width="400" height="400">
  <img src="https://i.pinimg.com/236x/4e/e0/e7/4ee0e7ac0cd0a9dea3925e106f65e6bf.jpg" alt="Falls" width="400" height="400">
  <img src="https://i.pinimg.com/564x/24/58/35/245835be9c23261523858a643af3aaf2.jpg" alt="Falls" width="400" height="400">
  <img src="https://i.pinimg.com/236x/e6/ce/7d/e6ce7d9465c46a3a53906f917196f152.jpg" alt="Ocean" width="400" height="400">
  <img src="https://i.pinimg.com/236x/8d/40/5a/8d405a46fec33b0be9c8d3d397dda3af.jpg" alt="Ocean II" width="400" height="400">
  <img src="https://i.pinimg.com/236x/65/9a/47/659a4724c4eeb0b246a5656123c515fd.jpg" alt="Falls" width="400" height="400">
  <img src="https://i.pinimg.com/236x/d8/1d/1d/d81d1dbed1f31fce8b7e5a45f297ee41.jpg" alt="Falls" width="400" height="400">
  <img src="https://i.pinimg.com/236x/fd/12/91/fd12913321d022946927cd0e555b1143.jpg" alt="Falls" width="400" height="400">
  <img src="https://i.pinimg.com/236x/0f/49/47/0f494706612bcfb9014da69f0d4567a5.jpg" alt="Falls" width="400" height="400">
</div>




  <!-- Contact -->
  <div class="w3-light-grey w3-padding-large w3-padding-32 w3-margin-top" id="contact">
    <h3 class="w3-center">Contact</h3>
    <hr>
    <p>We value your opinion and would love to hear from you! As a passionate cricket fan, your feedback is critical in helping us deliver the best possible analysis and insights. Please take a moment to share your thoughts on our website, and let us know how we can continue to improve your experience. Thank you for your support!</p>

    <form action="/action_page.php" target="_blank">
      <div class="w3-section">
        <label>Name</label>
        <input class="w3-input w3-border" type="text" required name="Name">
      </div>
      <div class="w3-section">
        <label>Email</label>
        <input class="w3-input w3-border" type="text" required name="Email">
      </div>
      <div class="w3-section">
        <label>Feedback</label>
        <input class="w3-input w3-border" required name="Message">
      </div>
      <button type="submit" class="w3-button w3-block w3-dark-grey">Send</button>
    </form><br>
    <p>Powered by <a href="CRA" target="_blank" class="w3-hover-text-green">CRA</a></p>

  </div>

<!-- End page content -->
</div>

</body>
</html>

    """
    return HTMLResponse(content = my_homepage)


@app.get("/pointstable")
def get_pointstable():
    my_pointstable = """
    <!DOCTYPE html>
<html>
<head>
  <style>
    nav {
  display: flex;
  justify-content: space-between;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

li:first-child {
  margin-left: 0;
}

li:last-child {
  margin-right: 0;
}

  </style>
  <nav>
  <ul>
    <li><a href="http://127.0.0.1:8000/">Home</a></li>
    <li><a href="http://127.0.0.1:8000/wicket">Highest Wickets</a></li>
    <li><a href="http://127.0.0.1:8000/video">Video</a></li>
    <li><a href="http://127.0.0.1:8000/pointstable">Points Table</a></li>
    <li><a href="http://127.0.0.1:8000/batsman">Batsman</a></li>
    <li><a href="http://127.0.0.1:8000/centuries">Centuries</a></li>
    <li><a href="http://127.0.0.1:8000/sponsors">Sponsors</a></li>
    <li><a href="http://127.0.0.1:8000/News">News</a></li>
    <li><a href="http://127.0.0.1:8000/about">About Us</a></li>
  </ul>
</nav>

	<title>IPL Team Points Table</title>
	<style>
		table {
			border-collapse: collapse;
			width: 100%;
			font-family: Arial, sans-serif;
			font-size: 14px;
			text-align: center;
		}
		th, td {
			padding: 10px;
			border: 1px solid #ccc;
			color: #333;
		}
		th {
			background-color: #f2f2f2;
			font-weight: bold;
			color: #555;
		}
		tr:nth-child(even) {
			background-color: #f2f2f2;
		}
	</style>
</head>
<body>
	<h1>EX: IPL 2023 Points Table</h1>
	<table>
		<thead>

			<tr>
				<th>Team</th>
				<th>Matches Played</th>
				<th>Matches Won</th>
				<th>Matches Lost</th>
				<th>No Result/Tie</th>
				<th>Points</th>
				<th>Net Run Rate</th>
			</tr>
		</thead>
		<tbody>
		    <tr>
				<td>Gujarat Titans</td>
				<td>14</td>
				<td>10</td>
				<td>4</td>
				<td>0</td>
				<td>20</td>
				<td>0.361</td>
			</tr>
			<tr>
				<td>Rajasthan Royals</td>
				<td>14</td>
				<td>9</td>
				<td>5</td>
				<td>0</td>
				<td>18</td>
				<td>0.298</td>
			</tr>
			<tr>
				<td>lucknow super giants</td>
				<td>14</td>
				<td>9</td>
				<td>5</td>
				<td>0</td>
				<td>18</td>
				<td>0.251</td>
			</tr>
			<tr>
				<td>Royal Challengers Bangalore</td>
				<td>14</td>
				<td>8</td>
				<td>6</td>
				<td>0</td>
				<td>16</td>
				<td>-0.253</td>
			</tr>
			<tr>
				<td>Delhi Capitals</td>
				<td>14</td>
				<td>7</td>
				<td>7</td>
				<td>0</td>
				<td>14</td>
				<td>0.204</td>
			</tr>
			<tr>
				<td>Punjab Kings</td>
				<td>14</td>
				<td>7</td>
				<td>7</td>
				<td>0</td>
				<td>14</td>
				<td>0.126</td>
			</tr>
			<tr>
				<td>Kolkata Knight Riders</td>
				<td>14</td>
				<td>6</td>
				<td>8</td>
				<td>0</td>
				<td>12</td>
				<td>0.146</td>
			</tr>

			<tr>
				<td>Sunrisers Hydrabad</td>
				<td>14</td>
				<td>6</td>
				<td>8</td>
				<td>0</td>
				<td>12</td>
				<td>-0.379</td>
			</tr>
			<tr>
				<td>Chennai Super Kings</td>
				<td>14</td>
				<td>4</td>
				<td>10</td>
				<td>0</td>
				<td>8</td>
				<td>-0.203</td>
			</tr>
			<tr>
				<td>Mumbai Indians</td>
				<td>14</td>
				<td>4</td>
				<td>10</td>
				<td>0</td>
				<td>20</td>
				<td>-0.506</td>
			</tr>
    """
    return HTMLResponse(content = my_pointstable)


@app.get("/batsman")
def get_batsman():
    my_batsman = """
    <!DOCTYPE html>
<html>
  <head>
    <title>Top Batsmen in IPL</title>
      <style>
    nav {
  display: flex;
  justify-content: space-between;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

li:first-child {
  margin-left: 0;
}

li:last-child {
  margin-right: 0;
}

  </style>
  <nav>
  <ul>
    <li><a href="http://127.0.0.1:8000/">Home</a></li>
    <li><a href="http://127.0.0.1:8000/wicket">Highest Wickets</a></li>
    <li><a href="http://127.0.0.1:8000/video">Video</a></li>
    <li><a href="http://127.0.0.1:8000/pointstable">Points Table</a></li>
    <li><a href="http://127.0.0.1:8000/batsman">Batsman</a></li>
    <li><a href="http://127.0.0.1:8000/centuries">Centuries</a></li>
    <li><a href="http://127.0.0.1:8000/sponsors">Sponsors</a></li>
    <li><a href="http://127.0.0.1:8000/News">News</a></li>
    <li><a href="http://127.0.0.1:8000/about">About Us</a></li>
  </ul>
</nav>

    <style>
      table {
        border-collapse: collapse;
        width: 100%;
      }
      th, td {
        text-align: left;
        padding: 8px;
        border-bottom: 1px solid #ddd;
      }
      th {
        background-color: #f2f2f2;
      }
      tr:nth-child(even) {
        background-color: #f2f2f2;
      }
    </style>
  </head>
  <body>
    <h1>Top Batsmen in IPL</h1>
    <table>
      <thead>
        <tr>
          <th>Rank</th>
          <th>Player Name</th>
          <th>Team</th>
          <th>Matches</th>
          <th>Runs</th>
          <th>Average</th>
          <th>Strike Rate</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>Virat Kohli</td>
          <td>Royal Challengers Bangalore</td>
          <td>199</td>
          <td>6076</td>
          <td>37.97</td>
          <td>130.41</td>
        </tr>
        <tr>
          <td>2</td>
          <td>Suresh Raina</td>
          <td>Chennai Super Kings</td>
          <td>207</td>
          <td>5448</td>
          <td>33.34</td>
          <td>137.14</td>
        </tr>
        <tr>
          <td>3</td>
          <td>David Warner</td>
          <td>Sunrisers Hyderabad</td>
          <td>148</td>
          <td>5447</td>
          <td>42.22</td>
          <td>142.39</td>
        </tr>
        <tr>
          <td>4</td>
          <td>Rohit Sharma</td>
          <td>Mumbai Indians</td>
          <td>207</td>
          <td>5431</td>
          <td>31.27</td>
          <td>130.61</td>
        </tr>
        <tr>
          <td>5</td>
          <td>Shikhar Dhawan</td>
          <td>Delhi Capitals</td>
          <td>176</td>
          <td>5428</td>
          <td>34.81</td>
          <td>126.82</td>
        </tr>
        <tr>
          <td>6</td>
          <td>Chris Gayle</td>
          <td>Punjab Kings</td>
          <td>149</td>
          <td>4950</td>
          <td>40.24</td>
          <td>149.94</td>
        </tr>
        <tr>
          <td>7</td>
          <td>AB de Villiers</td>
          <td>Royal Challengers Bangalore</td>
          <td>176</td>
          <td>4985</td>
          <td>40.77</td>
          <td>151.23</td>
        </tr>
        <tr>
          <td>8</td>
          <td>MS Dhoni</td>
          <td>Chennai Super Kings</td>
          <td>211</td>
          <td>4632</td>
          <td>42.21</td>
          <td>136.75</td>
        </tr>
        <tr>
          <td>9</td>
          <td>Rishabh Pant</td>
          <td>Delhi Capitals</td>
          <td>87</td>
          <td>2578</td>
          <td>35.11</td>
          <td>148.73</td>
        </tr>
        <tr>
          <td>10</td>
          <td>Ravindra Jadeja</td>
          <td>Chennai Super Kings</td>
          <td>184</td>
          <td>2398</td>
          <td>23.64</td>
          <td>126.86</td>
        </tr>
        <tr>
          <td>11</td>
          <td>Shane Watson</td>
          <td>Chennai Super Kings</td>
          <td>145</td>
          <td>3874</td>
          <td>30.99</td>
          <td>139.53</td>
        </tr>
        <tr>
          <td>12</td>
          <td>Gautam Gambhir</td>
          <td>Kolkata Knight Riders</td>
          <td>154</td>
          <td>4217</td>
          <td>31.23</td>
          <td>123.88</td>
        </tr>
        <tr>
          <td>13</td>
          <td>Yuvraj Singh</td>
          <td>Punjab Kings</td>
          <td>132</td>
          <td>2750</td>
          <td>24.77</td>
          <td>129.71</td>
        </tr>
        <tr>
          <td>14</td>
          <td>Robin Uthappa</td>
          <td>Rajasthan Royals</td>
          <td>189</td>
          <td>4607</td>
          <td>27.92</td>
          <td>129.99</td>
        </tr>
        <tr>
          <td>15</td>
          <td>David Miller</td>
          <td>Rajasthan Royals</td>
          <td>87</td>
          <td>2210</td>
          <td>33.03</td>
          <td>140.06</td>
        </tr>
        <tr>
          <td>16</td>
          <td>Manish Pandey</td>
          <td>Sunrisers Hyderabad</td>
          <td>148</td>
          <td>3863</td>
          <td>29.3</td>
          <td>121.31</td>
        </tr>
        <tr>
          <td>17</td>
          <td>Shane Warne</td>
          <td>Rajasthan Royals</td>
          <td>55</td>
          <td>345</td>
          <td>7.85</td>
          <td>103.25</td>
        </tr>





      </tbody> 
    </table>
  </body>
</html>     
    """
    return HTMLResponse(content = my_batsman)


@app.get("/wicket")
def get_wicket():
    wicket = """
    <!DOCTYPE html>
<html>
  <head>
    <style>
    nav {
  display: flex;
  justify-content: space-between;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

li:first-child {
  margin-left: 0;
}

li:last-child {
  margin-right: 0;
}

  </style>
  <nav>
  <ul>
    <li><a href="http://127.0.0.1:8000/">Home</a></li>
    <li><a href="http://127.0.0.1:8000/wicket">Highest Wickets</a></li>
    <li><a href="http://127.0.0.1:8000/video">Video</a></li>
    <li><a href="http://127.0.0.1:8000/pointstable">Points Table</a></li>
    <li><a href="http://127.0.0.1:8000/batsman">Batsman</a></li>
    <li><a href="http://127.0.0.1:8000/centuries">Centuries</a></li>
    <li><a href="http://127.0.0.1:8000/sponsors">Sponsors</a></li>
    <li><a href="http://127.0.0.1:8000/News">News</a></li>
    <li><a href="http://127.0.0.1:8000/about">About Us</a></li>
  </ul>
</nav>

    <title>Highest Wicket Takers in IPL</title>
  </head>
  <body>
    <h1>Highest Wicket Takers in IPL</h1>
    <style>
      table {
        border-collapse: collapse;
        width: 100%;
      }
      th, td {
        text-align: left;
        padding: 8px;
        border-bottom: 1px solid #ddd;
      }
      th {
        background-color: #f2f2f2;
      }
      tr:nth-child(even) {
        background-color: #f2f2f2;
      }
    </style>
    <table>
      <thead>
        <tr>
          <th>Player Name</th>
          <th>Team</th>
          <th>Matches</th>
          <th>Wickets</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Lasith Malinga</td>
          <td>Mumbai Indians</td>
          <td>122</td>
          <td>170</td>
        </tr>
        <tr>
          <td>Amit Mishra</td>
          <td>Delhi Capitals</td>
          <td>159</td>
          <td>166</td>
        </tr>
        <tr>
          <td>Piyush Chawla</td>
          <td>Mumbai Indians</td>
          <td>164</td>
          <td>164</td>
        </tr>
        <tr>
          <td>Harbhajan Singh</td>
          <td>Chennai Super Kings</td>
          <td>160</td>
          <td>162</td>
        </tr>
        <tr>
          <td>Dwayne Bravo</td>
          <td>Chennai Super Kings</td>
          <td>140</td>
          <td>156</td>
        </tr>
        <tr>
        <td>Kagiso Rabada</td>
        <td>Delhi Capitals</td>
        <td>49</td>
        <td>61</td>
      </tr>
      <tr>
        <td>Bhuvneshwar Kumar</td>
        <td>Sunrisers Hyderabad</td>
        <td>121</td>
        <td>136</td>
      </tr>
      <tr>
        <td>Ravindra Jadeja</td>
        <td>Chennai Super Kings</td>
        <td>204</td>
        <td>119</td>
      </tr>
      <tr>
        <td>Sunil Narine</td>
        <td>Kolkata Knight Riders</td>
        <td>120</td>
        <td>125</td>
      </tr>
      <tr>
        <td>Umesh Yadav</td>
        <td>Delhi Capitals</td>
        <td>121</td>
        <td>119</td>
      </tr>
      <tr>
  <td>Yuzvendra Chahal</td>
  <td>Royal Challengers Bangalore</td>
  <td>100</td>
  <td>125</td>
</tr>
<tr>
  <td>Bhuvneshwar Kumar</td>
  <td>Sunrisers Hyderabad</td>
  <td>121</td>
  <td>136</td>
</tr>
<tr>
  <td>Jasprit Bumrah</td>
  <td>Mumbai Indians</td>
  <td>99</td>
  <td>115</td>
</tr>
<tr>
  <td>Mohammed Shami</td>
  <td>Punjab Kings</td>
  <td>87</td>
  <td>91</td>
</tr>
<tr>
  <td>Kuldeep Yadav</td>
  <td>Kolkata Knight Riders</td>
  <td>76</td>
  <td>77</td>
</tr>
<tr>
  <td>Rashid Khan</td>
  <td>Sunrisers Hyderabad</td>
  <td>62</td>
  <td>75</td>
</tr>
<tr>
  <td>Imran Tahir</td>
  <td>Chennai Super Kings</td>
  <td>55</td>
  <td>79</td>
</tr>
<tr>
  <td>Mitchell McClenaghan</td>
  <td>Mumbai Indians</td>
  <td>56</td>
  <td>71</td>
</tr>
<tr>
  <td>Sandeep Sharma</td>
  <td>Hyderabad Sunrisers</td>
  <td>98</td>
  <td>109</td>
</tr>
<tr>
  <td>Mohit Sharma</td>
  <td>Punjab Kings</td>
  <td>89</td>
  <td>91</td>
</tr>

      </tbody>
    </table>
  </body>
</html>
"""
    return HTMLResponse(content = wicket)


@app.get("/centuries")
def get_centuries():
    my_100 = """
    <!DOCTYPE html>
<html>
  <head>
  <style>
    nav {
  display: flex;
  justify-content: space-between;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

li:first-child {
  margin-left: 0;
}

li:last-child {
  margin-right: 0;
}

  </style>
  <nav>
  <ul>
    <li><a href="http://127.0.0.1:8000/">Home</a></li>
    <li><a href="http://127.0.0.1:8000/wicket">Highest Wickets</a></li>
    <li><a href="http://127.0.0.1:8000/video">Video</a></li>
    <li><a href="http://127.0.0.1:8000/pointstable">Points Table</a></li>
    <li><a href="http://127.0.0.1:8000/batsman">Batsman</a></li>
    <li><a href="http://127.0.0.1:8000/centuries">Centuries</a></li>
    <li><a href="http://127.0.0.1:8000/sponsors">Sponsors</a></li>
    <li><a href="http://127.0.0.1:8000/News">News</a></li>
    <li><a href="http://127.0.0.1:8000/about">About Us</a></li>
  </ul>
</nav>

    <title>Top centuries</title>
  </head>
  <body>
    <h1>Top centuries</h1>
    <style>
      table {
        border-collapse: collapse;
        width: 100%;
      }
      th, td {
        text-align: left;
        padding: 8px;
        border-bottom: 1px solid #ddd;
      }
      th {
        background-color: #f2f2f2;
      }
      tr:nth-child(even) {
        background-color: #f2f2f2;
      }
    </style>
    <table>
  <tr>
    <th>Rank</th>
    <th>Player</th>
    <th>Team</th>
    <th>Matches</th>
    <th>Runs</th>
    <th>Average</th>
    <th>100s</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Chris Gayle</td>
    <td>Punjab Kings</td>
    <td>149</td>
    <td>4950</td>
    <td>40.24</td>
    <td>6</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Virat Kohli</td>
    <td>Royal Challengers Bangalore</td>
    <td>199</td>
    <td>6076</td>
    <td>37.97</td>
    <td>5</td>
  </tr>
  <tr>
    <td>3</td>
    <td>David Warner</td>
    <td>Sunrisers Hyderabad</td>
    <td>148</td>
    <td>5447</td>
    <td>42.22</td>
    <td>4</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Shane Watson</td>
    <td>Chennai Super Kings</td>
    <td>145</td>
    <td>3874</td>
    <td>30.99</td>
    <td>4</td>
  </tr>
  <tr>
    <td>5</td>
    <td>David Miller</td>
    <td>Rajasthan Royals</td>
    <td>87</td>
    <td>2133</td>
    <td>33.25</td>
    <td>2</td>
  </tr>
  <tr>
    <td>6</td>
    <td>AB de Villiers</td>
    <td>Royal Challengers Bangalore</td>
    <td>176</td>
    <td>4985</td>
    <td>40.77</td>
    <td>2</td>
  </tr>
  <tr>
    <td>7</td>
    <td>David Warner</td>
    <td>Sunrisers Hyderabad</td>
    <td>148</td>
    <td>5447</td>
    <td>42.22</td>
    <td>2</td>
  </tr>
  <tr>
    <td>8</td>
    <td>KL Rahul</td>
    <td>Punjab Kings</td>
    <td>84</td>
    <td>2647</td>
    <td>44.17</td>
    <td>2</td>
  </tr>
  <tr>
    <td>9</td>
    <td>Sanju Samson</td>
    <td>Rajasthan Royals</td>
    <td>107</td>
    <td>2584</td>
    <td>27.95</td>
    <td>2</td>
  </tr>
  <tr>
    <td>10</td>
    <td>Rohit Sharma</td>
    <td>Mumbai Indians</td>
    <td>207</td>
    <td>5103</td>
    <td>48.25</td>
    <td>2</td>
  </tr>
  </table>  


  </body>
</html>
"""
    return HTMLResponse(content = my_100)


@app.get("/video")
def get_video():
    videos = """
    <head>
    <style>
    nav {
  display: flex;
  justify-content: space-between;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

li:first-child {
  margin-left: 0;
}

li:last-child {
  margin-right: 0;
}

  </style>
  <nav>
  <ul>
    <li><a href="http://127.0.0.1:8000/">Home</a></li>
    <li><a href="http://127.0.0.1:8000/wicket">Highest Wickets</a></li>
    <li><a href="http://127.0.0.1:8000/video">Video</a></li>
    <li><a href="http://127.0.0.1:8000/pointstable">Points Table</a></li>
    <li><a href="http://127.0.0.1:8000/batsman">Batsman</a></li>
    <li><a href="http://127.0.0.1:8000/centuries">Centuries</a></li>
    <li><a href="http://127.0.0.1:8000/sponsors">Sponsors</a></li>
    <li><a href="http://127.0.0.1:8000/News">News</a></li>
    <li><a href="http://127.0.0.1:8000/about">About Us</a></li>
  </ul>
</nav>
		</head>
    <section class="video-section">
  <div class="container">
    <h2 class="section-title">IPL Best Highlights</h2>
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/videoseries?list=PLzCcVGorhvJX9z6up-2QBuHlBTJuoUAZ_" frameborder="0" allowfullscreen></iframe>
    </div>
  </div>
</section>
"""
    return HTMLResponse(content = videos)



@app.get("/about")
def about():
    about = """
    <!DOCTYPE html>
<html>

<head>
	<title>About Us | CRA</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<style>
		/* Insert your CSS styles here */
	</style>
</head>
<body>
<style>
    nav {
  display: flex;
  justify-content: space-between;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

li:first-child {
  margin-left: 0;
}

li:last-child {
  margin-right: 0;
}

  </style>
  <nav>
  <ul>
    <li><a href="http://127.0.0.1:8000/">Home</a></li>
    <li><a href="http://127.0.0.1:8000/wicket">Highest Wickets</a></li>
    <li><a href="http://127.0.0.1:8000/video">Video</a></li>
    <li><a href="http://127.0.0.1:8000/pointstable">Points Table</a></li>
    <li><a href="http://127.0.0.1:8000/batsman">Batsman</a></li>
    <li><a href="http://127.0.0.1:8000/centuries">Centuries</a></li>
    <li><a href="http://127.0.0.1:8000/sponsors">Sponsors</a></li>
    <li><a href="http://127.0.0.1:8000/News">News</a></li>
    <li><a href="http://127.0.0.1:8000/about">About Us</a></li>
  </ul>
</nav>
	<header>
		<h1>Cricket Research Analysis</h1>
		<p>Analyze your way to victory!</p>
	</header>

	<main>
		<section>
			<h2>About Us</h2>
			<p>Cricket Analyst is a web application designed to provide cricket fans and analysts with the latest news, analysis, and statistics on all major cricket tournaments around the world.</p>
			<p>Our team of experienced cricket analysts and statisticians work around the clock to provide our users with up-to-date information and insights that they can use to make informed decisions and gain a competitive edge.</p>
			<p>Whether you're a casual cricket fan or a seasoned analyst, Cricket Analyst has everything you need to stay on top of your game.</p>
		</section>

		<section>
			<h2>Our Team</h2>
			<ul>
				<li><strong>Jenith Suvagia</strong> - Chief Analyst</li>
				<li><strong>Venkat</strong> - Lead Statistician</li>
				<li><strong>Rutvik</strong> - Senior Writer</li>
			</ul>
		</section>

		<section>
			<h2>Our Mission</h2>
			<p>Our mission is to provide cricket fans and analysts with the most comprehensive and accurate information and insights on all major cricket tournaments around the world.</p>
			<p>We believe that by providing our users with the tools they need to make informed decisions and gain a competitive edge, we can help them achieve their goals and reach their full potential.</p>
		</section>
	</main>

	<footer>
		<p>&copy; 2023 Cricket Research Analysis . All rights reserved.</p>
	</footer>
</body>
</html>
"""
    return HTMLResponse(content = about)


@app.get("/News")
def News():
    news = """
    <!DOCTYPE html>
<html>
  <head>
    <title>CFA Latest News and Announcements</title>
  </head>
  <style>
    nav {
  display: flex;
  justify-content: space-between;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

li:first-child {
  margin-left: 0;
}

li:last-child {
  margin-right: 0;
}

  </style>
  <nav>
  <ul>
    <li><a href="http://127.0.0.1:8000/">Home</a></li>
    <li><a href="http://127.0.0.1:8000/wicket">Highest Wickets</a></li>
    <li><a href="http://127.0.0.1:8000/video">Video</a></li>
    <li><a href="http://127.0.0.1:8000/pointstable">Points Table</a></li>
    <li><a href="http://127.0.0.1:8000/batsman">Batsman</a></li>
    <li><a href="http://127.0.0.1:8000/centuries">Centuries</a></li>
    <li><a href="http://127.0.0.1:8000/sponsors">Sponsors</a></li>
    <li><a href="http://127.0.0.1:8000/News">News</a></li>
    <li><a href="http://127.0.0.1:8000/about">About Us</a></li>
  </ul>
</nav>

  <body>
    <h1>CFA Latest News and Announcements</h1>

    <h2>Latest News</h2>
    <ul>
      <li><a href="https://www.iplt20.com/news/3860/bcci-announces-schedule-for-tata-ipl-2023">BCCI announces schedule for TATA IPL 2023</a></li>
      <li><a href="https://www.iplt20.com/news/3860/bcci-announces-schedule-for-tata-ipl-2023">Lockie Ferguson and Rahmanullah Gurbaz traded from Gujarat Titans to Kolkata Knight Riders</a></li>
      <li><a href="https://www.iplt20.com/news/3859/bcci-announces-the-release-of-request-for-proposals-for-staging-fan-parks-for-the-indian-premier-league-seasons-2023-2024-and-2025">Board of Control for Cricket in India (BCCI) announces the release of Request for Proposals for staging fan parks for the Indian Premier League Seasons 2023, 2024 and 2025</a></li>
    </ul>

    <h2>Announcements</h2>
    <ul>
      <li>Announcement 1</li>
      <li>Announcement 2</li>
      <li>Announcement 3</li>
    </ul>

  </body>
</html>
    """
    return HTMLResponse(content = news)


@app.get("/sponsors")
def get_sponsors():
    sponsors = """
    <!DOCTYPE html>
<html>
  <head>
    <title>Our Sponsors and Proud Partners</title>
      <style>
    nav {
  display: flex;
  justify-content: space-between;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

li:first-child {
  margin-left: 0;
}

li:last-child {
  margin-right: 0;
}

  </style>
  <nav>
  <ul>
    <li><a href="http://127.0.0.1:8000/">Home</a></li>
    <li><a href="http://127.0.0.1:8000/wicket">Highest Wickets</a></li>
    <li><a href="http://127.0.0.1:8000/video">Video</a></li>
    <li><a href="http://127.0.0.1:8000/pointstable">Points Table</a></li>
    <li><a href="http://127.0.0.1:8000/batsman">Batsman</a></li>
    <li><a href="http://127.0.0.1:8000/centuries">Centuries</a></li>
    <li><a href="http://127.0.0.1:8000/sponsors">Sponsors</a></li>
    <li><a href="http://127.0.0.1:8000/News">News</a></li>
    <li><a href="http://127.0.0.1:8000/about">About Us</a></li>
  </ul>
</nav>
    <style>
      /* Align images in a row */
      img {
        display: inline-block;
        margin: 10px;
      }
    </style>  
  </head>
  <body>
    <h1>Our Sponsors and Proud Partners</h1>

    <!-- Logo and branding section -->
    <section>
      <h2>Logos and Branding</h2>
      <img src="https://i.pinimg.com/564x/a9/9c/dc/a99cdcd8e634e82f6ba692bfea588016.jpg" alt="Partner 1 Logo"  width="400" height="400">
      <img src="https://logos-download.com/wp-content/uploads/2021/01/University_of_the_Pacific_Logo.png" alt="Partner 2 Logo"  width="400" height="400">
      <img src="https://i.pinimg.com/564x/a9/9c/dc/a99cdcd8e634e82f6ba692bfea588016.jpg" alt="Sponsor 1 Logo"  width="400" height="400">
      <img src="https://logos-download.com/wp-content/uploads/2021/01/University_of_the_Pacific_Logo.png" alt="Sponsor 2 Logo"  width="400" height="400">
      <img src="https://i.pinimg.com/564x/a9/9c/dc/a99cdcd8e634e82f6ba692bfea588016.jpg" alt="Sponsor 1 Logo"  width="400" height="400">
      <img src="https://logos-download.com/wp-content/uploads/2021/01/University_of_the_Pacific_Logo.png" alt="Sponsor 2 Logo"  width="400" height="400">  
    </section>

    <!-- Partnership/sponsorship description section -->
    <section>
      <h2>Partnership/Sponsorship Description</h2>
      <h3>Partner 1</h3>
      <p>Discover your passion and unlock your potential at the University of the Pacific.</p>

      <h3>Partner 2</h3>
      <p>From small class sizes to a personalized approach to learning, the University of the Pacific is committed to your success.</p>

      <h3>Sponsor 1</h3>
      <p>At the University of the Pacific, we believe that education is not just about knowledge, but also about character and values.</p>

      <h3>Sponsor 2</h3>
      <p>Become part of a vibrant and diverse community of learners at the University of the Pacific and prepare for a bright future.</p>
    </section>

    <!-- Testimonials section -->
    <section>
      <h2>Testimonials</h2>
      <blockquote>
        "As a sponsor of the cricket analysis research web application, I am impressed by the depth and accuracy of the data provided. The analysis and insights generated by this web application are invaluable for both players and fans, and the level of detail and precision is unmatched in the industry. I believe that this tool will become an essential resource for anyone interested in cricket, and I am proud to support its development. The team behind this web application is clearly dedicated to advancing the sport and enhancing the experience of its fans, and I look forward to seeing the impact it will have on the cricket world."
        <cite>– Partner 1</cite>
      </blockquote>

      <blockquote>
        "As a sponsor of the cricket analysis research web application, I am thrilled to be supporting cutting-edge research that is revolutionizing the way we understand and analyze this dynamic sport. This web application provides valuable insights and data-driven analysis that can help teams and players at all levels improve their performance and achieve their goals. I am proud to be associated with such an innovative and forward-thinking project, and I am confident that it will have a significant impact on the future of cricket."
        <cite>– Sponsor 1</cite>
      </blockquote>
    </section>

    <!-- Benefits section -->
    <section>
      <h2>Benefits of Partnership/Sponsorship</h2>
      <ul>
        <li>Increased brand visibility</li>
        <li>Access to a specific audience</li>
        <li>Promotion on our website and social media channels</li>
        <li>Opportunities for co-branded events and campaigns</li>
      </ul>
    </section>

    <!-- Call to action section -->
    <section>
      <h2>Interested in becoming a partner or sponsor?</h2>
      <p>Contact us to learn more about partnership and sponsorship opportunities.</p>
      <a href="http://127.0.0.1:8000/#contact"><button>Contact Us</button></a>

"""
    return HTMLResponse(content = sponsors)

@app.get("/wickets")
async def get_wickets():
    return data1


# Endpoint to retrieve products by Bolwer
@app.get('/wickets/{BowlerName}')
async def get_wickets_by_name(BowlerName: str):
    wickets = [wickets for wickets in data1 if wickets['BowlerName'].lower() == BowlerName.lower()]
    if len(wickets) == 0:
        return {'message': 'No products found'}
    return wickets


@app.get("/runs")
async def get_runs():
    return data2


# Endpoint to retrieve most SR by StrikerName
@app.get('/runs/{StrikerName}')
async def get_runs(StrikerName: str):
    runs = [runs for runs in data2 if runs['StrikerName'].lower() == StrikerName.lower()]
    if len(runs) == 0:
        return {'message': 'No products found'}
    return runs


@app.get("/bowling")
async def get_bowling():
    return data3


# Endpoint to retrieve most Centuries by Number of StrikerName
@app.get('/bowling/{BowlerName}')
async def get_bowling(BowlerName: str):
    bowling = [bowling for bowling in data3 if bowling['BowlerName'].lower() == BowlerName.lower()]
    if len(bowling) == 0:
        return {'message': 'No products found'}
    return bowling
