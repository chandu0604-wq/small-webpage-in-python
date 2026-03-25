from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Profile</title>
#         <style>
#             body {
#                 margin: 0;
#                 font-family: Arial;
#                 background: #0f172a;
#                 color: white;
#             }

#             .navbar {
#                 display: flex;
#                 justify-content: space-between;
#                 align-items: center;
#                 background: #1e293b;
#                 padding: 15px 30px;
#             }

#             .nav-links a {
#                 color: white;
#                 text-decoration: none;
#                 margin: 0 15px;
#             }

#             .nav-links a:hover {
#                 color: #38bdf8;
#             }

#             .container {
#                 text-align: center;
#                 padding: 40px;
#             }

#             h1 {
#                 margin-bottom: 10px;
#             }

#             /* Skills */
#             .skills {
#                 margin-top: 40px;
#             }

#             .skill-box {
#                 display: inline-block;
#                 background: #1e293b;
#                 padding: 10px 15px;
#                 margin: 8px;
#                 border-radius: 20px;
#                 font-size: 14px;
#                 transition: 0.3s;
#             }

#             .skill-box:hover {
#                 background: #38bdf8;
#                 color: black;
#                 transform: scale(1.1);
#             }

#             /* Links */
#             .places a {
#                 display: block;
#                 margin: 15px;
#                 padding: 12px;
#                 color: white;
#                 text-decoration: none;
#                 border-radius: 8px;
#                 width: 220px;
#                 margin-left: auto;
#                 margin-right: auto;
#                 transition: 0.3s;
#             }

#             .linkedin { background-color: #0077b5; }
#             .linkedin:hover { background-color: #005582; }

#             .github { background-color: #171515; }
#             .github:hover { background-color: #333; }

#             .nextwave {
#                 background-color: #38bdf8;
#                 color: black;
#             }

#             .nextwave:hover {
#                 background-color: #0ea5e9;
#             }

#         </style>
#     </head>

#     <body>

#         <div class="navbar">
#             <div>⚡ Social Profiles</div>
#             <div class="nav-links">
#                 <a href="/">Home</a>
#                 <a href="#skills">Skills</a>
#             </div>
#         </div>

#         <div class="container">
#             <h1>🚀 Hruthik Gowda</h1>
#             <p>Building AI Assistants & Automation Systems</p>

#             <div class="skills" id="skills">
#                 <h2>💡 Skills</h2>

#                 <div class="skill-box">Python</div>
#                 <div class="skill-box">Flask</div>
#                 <div class="skill-box">Selenium</div>
#                 <div class="skill-box">Automation</div>
#                 <div class="skill-box">AI Integration</div>
#                 <div class="skill-box">Speech Recognition</div>
#                 <div class="skill-box">PyAutoGUI</div>
#                 <div class="skill-box">Web Scraping</div>
#                 <div class="skill-box">Chrome Automation</div>
#             </div>

#             <div class="places">
#                 <a href="https://www.linkedin.com/in/hruthik-gowda-52a71030b/" class="linkedin">LinkedIn</a>
#                 <a href="https://github.com/chandu0604-wq" class="github">GitHub</a>
#                 <a href="https://learning.ccbp.in/course-library" class="nextwave">NextWave</a>
#             </div>

#         </div>

#     </body>
#     </html>
#     """  

# # 🚀 Run Server
# if __name__ == "__main__":
#     print("Starting Flask server...")
#     app.run(debug=True)
