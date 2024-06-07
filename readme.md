<!--
 * @Author: shihan
 * @Date: 2023-10-30 19:43:09
 * @version: 1.0
 * @description: 
-->
source .venv/bin/activate
flask run
pandoc test.txt -o test.pdf

• Student names: Shihan Fu, Zhuofan Huang

• A link to your deployed web app running on Vercel
    https://sse-sf.vercel.app/

• A link to the GitHub repository containing the source code
    https://github.com/Randi-f/SSE/tree/master

 pytest api/*.py
 black api/app.py
 flake8 api/*.py
 flake8 --ignore=E501 api/

 coursework 2



| Student name   | Doc Name | GitHub usernames |
| ------------- | ------------- |------------- |
| Shihan Fu      | sf23     | Ranfi-f          |
| Zhuofan Huang  | zh3423   | zh3423           |

• A link to the GitHub Ac ons dashboard in the GitHub repo containing the source code
	https://github.com/Randi-f/SSE/actions
	
• A link to the new route from Part 4 in your deployed web app running on Vercel
	https://sse-sf.vercel.app/query?q=dinosaurs

coursework 4

| Student name   | Doc Name | GitHub usernames |
| ------------- | ------------- |------------- |
| Shihan Fu 	 | sf23     | Ranfi-f          |
| Zhuofan Huang  | zh3423   | zh3423           |

• Your Player Name from the game
 Aoligei
 
• A link to the GitHub Ac ons dashboard in the GitHub repo containing the source code
https://github.com/Randi-f/SSE/actions

• The short summary outlined above
  
1.How/why did you win/lose?
  We won! Because we implemented the corresponding functions correct.
  
2.What was your strategy for deciding which sorts of requests to tackle first?
  According to the frequence of being requested. This means that the more frequenct a request is sent to our system, the higher the priority it has. If we firstly deal with these kinds of request, the system will no longer need to check other unneccessary validation.
  In our case, according to the result shown in the game website, we had the most max number request than the plus request. So we put the validation of the key words for max number request first.
  
3.How did you decide when to release?
  After the function is implemented and all the tests are passed, it is pushed to github. After the actions are done, it is released and deployed.
  
4.How many times did you release?
  For each implementation, we release once. So it is three times in total.
  
5.What was your average time between releases?
  It depends on the time spent on developing. On average, it takes 10-20 minutes.
  
6.How do you feel about the quality of the code that you wrote?
  Great.
 
7.Did writing tests help?
  Yes. It helps a lot since after passing the test, the result of the functions is guaranteed.
  It also reduces the developing time of deploying on local computers. In this case, we can use test functions to check whether the design goal is implemented without running "flask run" command and go to the url links.
  
8.Did you delete any code?
  Yes. As more functions are added, many codes can be combined to reduce the redundancy of codes.
  
9.How did you co-operate within your team?
  With face-to-face communication, we agreed on how to achieve each goal. Then with the help of github, we implement the new functions and deploy it and then release it.


coursework 5 
| Student name   | Doc Name | GitHub usernames |
| ------------- | ------------- |------------- |
| Shihan Fu      | sf23     | Ranfi-f          |
| Zhuofan Huang  | zh3423   | zh3423           |
| Xiaotian Zhang  | xz6917   | XiaotianZhangGitHub          |

• A link to the new page showing the new functionality in your deployed web app running on Vercel
https://sse-sf.vercel.app/exploregit

• If you did an extension for Part 6, a short description of what your new feature does.
1. implement the security of communicating with GitHub api
    We add a security list. If the user is one of "protected" user, then the server will send request to the api with a header which contains authentication information. In this way, we can guarantee the security of communicating.
2. using response from https://api.github.com/users/{USER_NAME} to generate cv
    After collectint username from the home page, we used "session" to store the information of username for further usage. The user can click the "Generate your own CV!" area to redirect to a new page. On this page, information gained from the other api "https://api.github.com/users/{USER_NAME}" would be shown on the screen in tables. In addition, we used the link and the html label "img" to show a profile photo.
