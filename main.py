from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
import json
with open("most-runs-till-2022.json") as a:
    data1 = json.load(a)  # runs
    with open("most-fifties-till-2022.json") as b:
        data2 = json.load(b)  # fifties
        with open("fastest50-till-2022.json") as c:
            data3 = json.load(c)  # fastest50
            with open("fastest100-till-2022.json") as d:
                data4 = json.load(d)  # fastest100
                with open("best-bowling-figs-till-2022.json") as e:
                    data5 = json.load(e)  # bowling
                    with open("most-fours-till-2022.json") as f:
                        data6 = json.load(f)  # fours
                        with open("most-sixes-till-2022.json") as g:
                            data7 = json.load(g)  # sixes
                            with open("most-maidens-till-2022.json") as h:
                                data8 = json.load(h)  # maidens
                                with open("most-wickets-till-2022.json") as i:
                                    data9 = json.load(i)  # wickets
                                    with open("most-SR-till-2022.json") as k:
                                        data10 = json.load(k)  # SR
                                        with open("most-100s-till-2022.json") as l:
                                            data11 = json.load(l)  # most100


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
      <div class="w3-display-Left w3-padding-large w3-border w3-wide w3-text-black w3-align:right">
        <h1 class="w3-hide-medium w3-hide-small w3-xxxlarge">CRA</h1>
        <h5 class="w3-hide-large" style="white-space:nowrap">JANE DOE</h5>
        <h3 class="w3-hide-medium w3-hide-small">Cricket Research Analysis</h3>
      </div>
      <img class="w3-image" src="https://i.pinimg.com/564x/c1/54/e3/c154e359f37ac6b1d2efce17e63448a0.jpg" alt="Me" width="600" height="400">



      <!-- Navbar (placed at the bottom of the header image) -->
      <div class="w3-bar w3-light-grey w3-round w3-display-bottommiddle w3-hide-small" style="bottom:-16px">
        <a href="#" class="w3-bar-item w3-button">Home</a>
        <a href="#portfolio" class="w3-bar-item w3-button">Portfolio</a>
        <a href="#contact" class="w3-bar-item w3-button">Contact</a>
      </div>
    </header>

    <!-- Navbar on small screens -->
    <div class="w3-center w3-light-grey w3-padding-16 w3-hide-large w3-hide-medium">
    <div class="w3-bar w3-light-grey">
      <a href="#" class="w3-bar-item w3-button">Home</a>
      <a href="#portfolio" class="w3-bar-item w3-button">Portfolio</a>
      <a href="#contact" class="w3-bar-item w3-button">Contact</a>
    </div>
    </div>
    <!-- Page content -->
    <div class="w3-content w3-padding-large w3-margin-top" id="portfolio">

      <!-- Images (Portfolio) -->
      <img src="https://i.pinimg.com/564x/93/44/80/9344800799339a47a254ad1f6c564c20.jpg" alt="Ocean" class="w3-image" width="500" height="500">
      <img src="https://i.pinimg.com/236x/eb/ab/c9/ebabc996f7ef6dee11400acd443b156f.jpg" alt="Ocean II" class="w3-image w3-margin-top" width="500" height="500">
      <img src="https://i.pinimg.com/236x/4e/e0/e7/4ee0e7ac0cd0a9dea3925e106f65e6bf.jpg" alt="Falls" class="w3-image w3-margin-top" width="500" height="500">
      <img src="https://i.pinimg.com/564x/24/58/35/245835be9c23261523858a643af3aaf2.jpg" alt="Skies" class="w3-image w3-margin-top" width="500" height="500">
      <img src="https://i.pinimg.com/236x/fd/12/91/fd12913321d022946927cd0e555b1143.jpg" alt="Mountains" class="w3-image w3-margin-top" width="500" height="500">
      <img src="https://i.pinimg.com/236x/0f/49/47/0f494706612bcfb9014da69f0d4567a5.jpg" alt="Ocean" class="w3-image" width="500" height="500">
      <img src="https://i.pinimg.com/236x/e6/ce/7d/e6ce7d9465c46a3a53906f917196f152.jpg" alt="Ocean II" class="w3-image w3-margin-top" width="500" height="500">
      <img src="https://i.pinimg.com/236x/8d/40/5a/8d405a46fec33b0be9c8d3d397dda3af.jpg" alt="Falls" class="w3-image w3-margin-top" width="500" height="500">
      <img src="https://i.pinimg.com/236x/65/9a/47/659a4724c4eeb0b246a5656123c515fd.jpg" alt="Skies" class="w3-image w3-margin-top" width="500" height="500">
      <img src="https://i.pinimg.com/236x/d8/1d/1d/d81d1dbed1f31fce8b7e5a45f297ee41.jpg" alt="Mountains" class="w3-image w3-margin-top" width="500" height="500">

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

@app.get("/runs") # rutvik json
async def get_runs():
    return data1
@app.get("/fifties")
async def get_fifties():
    return data2

@app.get("/50")
async def get_50():
    return data3

@app.get("/100")
async def get_100():
    return data4

@app.get("/pointtable")
def point_table():
    my_pointstable = """
        <!DOCTYPE html>
    <html>
    <head>
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
    				<td>Mumbai Indians</td>
    				<td>14</td>
    				<td>10</td>
    				<td>4</td>
    				<td>0</td>
    				<td>20</td>
    				<td>+1.107</td>
    			</tr>
    			<tr>
    				<td>Chennai Super Kings</td>
    				<td>14</td>
    				<td>8</td>
    				<td>6</td>
    				<td>0</td>
    				<td>16</td>
    				<td>+0.732</td>
    			</tr>
    			<tr>
    				<td>Delhi Capitals</td>
    				<td>14</td>
    				<td>8</td>
    				<td>6</td>
    				<td>0</td>
    				<td>16</td>
    				<td>+0.333</td>
    			</tr>
    			<tr>
    				<td>Royal Challengers Bangalore</td>
    				<td>14</td>
    				<td>7</td>
    				<td>7</td>
    				<td>0</td>
    				<td>14</td>
    				<td>-0.117</td>
    			</tr>
    			<tr>
    				<td>Kolkata Knight Riders</td>
    				<td>14</td>
    				<td>6</td>
    				<td>8</td>
    				<td>0</td>
    				<td>12</td>
    				<td>-0.167</td>
    			</tr>
    			<tr>
    				<td>Punjab Kings</td>
    				<td>14</td>
    				<td>6</td>
    				<td>8</td>
    				<td>0</td>
    				<td>12</td>
    				<td>-0.264</td>
    			</tr>
    			<tr>
    				<td>Rajasthan Royals</td>
    				<td>14</td>
    				<td>6</td>
    				<td>8</td>
    				<td>0</td>
    				<td>12</td>
    				<td>-0.441</td>
    			</tr>

        """
    return HTMLResponse(content = my_pointstable)


@app.get("/bowling") # venkant json
async def get_bowling():
    return data5

@app.get("/fours")
async def get_fours():
    return data6

@app.get("/sixes")
async def get_sixes():
    return data7

@app.get("/maidens")
async def get_maidens():
    return data8

@app.get("/teams")
def teams():
    return {"message": 'To keep fans up to date with the latest news and developments regarding their favorite cricket teams, this web application will provide real-time updates on team management changes and player trades. The application could source its data from various news outlets and official team sources to ensure that the information is accurate and up to date. The updates could be displayed on a dedicated page within the application, with separate tabs for each team. Fans could also subscribe to notifications for their favorite teams to receive alerts when new updates are posted. This would provide fans with a convenient and efficient way to stay informed about the latest developments within their favorite teams, enhancing their overall user experience and increasing their engagement with the application.'}


@app.get("/auction")
def auction():
    return {"message": 'To keep fans up to date with the latest news and developments regarding their favorite cricket teams, this web application will provide real-time updates on team management changes and player trades. The application could source its data from various news outlets and official team sources to ensure that the information is accurate and up to date. The updates could be displayed on a dedicated page within the application, with separate tabs for each team. Fans could also subscribe to notifications for their favorite teams to receive alerts when new updates are posted. This would provide fans with a convenient and efficient way to stay informed about the latest developments within their favorite teams, enhancing their overall user experience and increasing their engagement with the application.'}

@app.get("/wickets") #jenith json
async def get_wickets():
    wicket = """
        <!DOCTYPE html>
    <html>
      <head>
        <title>Highest Wicket Takers in IPL</title>
      </head>
      <body>
        <h1>Highest Wicket Takers in IPL</h1>
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
          </tbody>
        </table>
      </body>
    </html>
    """
    return HTMLResponse(content = wicket)

@app.get("/SR")
async def get_sr():
    return data10

@app.get("/most100")
async def get_most100():
    return data11

@app.get("/Announcement")
def Announcement():
    return {"message": 'To keep fans informed about the latest news and announcements related to player and team updates, this dedicated section will be added to a web application. The section could include news articles, press releases, and official statements from the teams and players. Each update could be displayed in a clear and concise format, with a title, summary, and link to the full article or statement. The section could be updated regularly to ensure that fans have access to the most current and relevant information. This would provide fans with a convenient and reliable source of information about player and team updates, helping to enhance their overall user experience and engagement with the application.'}

@app.get("/MatchReport")
def match_report():
    return {"message": 'A match report that is summary that provides an overview of the key events and highlights of the game. A match report will include information such as the final score, the leading run-scorers and wicket-takers, and any notable moments or incidents that occurred during the match. Match reports may also include quotes from players, coaches, and commentators, as well as analysis and commentary on the performance of the teams and players.'}

@app.get("/live")
def live():
    return {"message": 'Adding a link for live matches in a web application would be a valuable feature for cricket fans who want to follow the action in real-time. The link could direct users to a live streaming service, where they can watch the match live as it unfolds.'}

@app.get("/Bookingseat")
def booking_seat():
    return {"message": 'Integrating a stadium seat booking feature in our web application would allow cricket fans to conveniently book seats for upcoming matches at their nearest stadium. Fans would be able to view the availability of seats for specific matches and select their preferred seat based on their budget and location preference. The application could also provide a seating plan of the stadium, allowing users to choose their seats based on their desired location within the stadium.'}

@app.get("/Foodsection")
def food_section():
    return {"message": 'Integrating a food ordering feature in our web application in future would enable cricket fans to conveniently order food and beverages from their designated seats. Fans would be able to browse menus, place their orders and make payments online, reducing the need for physical queues and improving the overall match-day experience. The orders could then be delivered directly to the fans seats, allowing them to enjoy their food and beverages while watching the match'}

@app.get("/videos")
def videos():
    videos = """
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


@app.get("/About")
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
    	<header>
    		<nav>
    			<ul>
    				<li><a href="">Home</a></li>
    				<li><a href="">About Us</a></li>
    				<li><a href="">Contact Us</a></li>
    			</ul>
    		</nav>
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
