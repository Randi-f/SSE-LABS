import math
from flask import Flask, render_template, request, session
import requests

app = Flask(__name__, static_url_path="/SSE-LAB2_static", static_folder="./static")
app.secret_key = "12345678"


@app.route("/")
def hello_world():
    return render_template("index.html")
    # return "Hello , my new app!"


@app.route("/exploregit")
def exploregit():
    return render_template("exploreGit.html")
    # return "Hello , my new app!"


@app.route("/exploregitsubmit", methods=["POST"])
def exploregitsubmit():
    githubusername = request.form.get("githubUsername")
    session["github_username"] = githubusername
    url = "https://api.github.com/users/" + githubusername + "/repos"
    response = send_request_git(url, githubusername)
    print(session)
    hashes = []
    authors = []
    dates = []
    commit_messages = []
    # repos=[]
    if response.status_code == 200:
        repos = response.json()  # list
        for repo in repos:
            commit_url = (
                "https://api.github.com/repos/"
                + githubusername
                + "/"
                + repo["name"]
                + "/commits"
            )
            # print(repo["updated_time"])
            commit_response = send_request_git(commit_url, githubusername)
            if commit_response.status_code == 200:
                commits = commit_response.json()
                # print(commits[0]["author"])
                hashes.append(commits[0]["sha"])
                authors.append(commits[0]["commit"]["author"]["name"])
                dates.append(commits[0]["commit"]["author"]["date"])
                commit_messages.append(commits[0]["commit"]["message"])
        return render_template(
            "table.html",
            hashes=hashes,
            authors=authors,
            dates=dates,
            commit_messages=commit_messages,
            items=[repo["full_name"] for repo in repos],
            updated_times=[repo["updated_at"] for repo in repos],
        )

    else:
        # Handle the case where the request was not successful
        print(
            f"Failed to retrieve repositories for {githubusername}."
            + f"Status code: {response.status_code}"
        )
        return "false"

    # return "Hello," + githubusername + getRepoInfo()


def send_request_git(url, github_user_name):
    # if github_user_name == "randi-f":
    if github_user_name == " ":  # for vercel version, cannot explode access_token
        # 3. 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
        # 1. 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
        # 2. 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
        access_token = "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"  # 替换为您的GitHub个人访问令牌
        headers = {
            "Authorization": "token " + access_token,
            "Accept": "application/vnd.github+json",
        }
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url)
    return response


@app.route("/generatecv")
# def generate_cv():
#     url = "https://api.github.com/users/randi-f"
#     response=send_request_git(url, "")
#     data=response.json()
#     return render_template("cv.html", response=data)
def generate_cv():
    print(session)
    github_username = session.get("github_username")  # 尝试从会话中获取 github_username
    if github_username is not None:
        url = "https://api.github.com/users/" + github_username
        response = send_request_git(url, github_username)
        data = response.json()
        return render_template("cv.html", response=data)
        # return f'Welcome back, User {github_username}!'
    else:
        return "Cannot find your github_username, please go back to /exploregit page!"


@app.route("/getrepo")
def getRepoInfo():
    # access_token = "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"  # 替换为您的GitHub个人访问令牌
    access_token = "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"
    headers = {"Authorization": "token " + access_token}
    response = requests.get(
        "https://api.github.com/users/randi-f/repos", headers=headers
    )
    # url = "https://api.github.com/users/"+githubusername+"/repos"
    # response = requests.get("https://api.github.com/repos/randi-f/-/commits")
    if response.status_code == 200:
        repos = response.json()  # list
        # print(type(repos))
        # for repo in repos:
        #     print(repo["full_name"])
    # return render_template('table.html', items=[repo['full_name'] for repo in repos])
    return str(repos)


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    if input_age < "18":
        return render_template("hello.html", name=input_name, age=input_age)
    else:
        return render_template("helloAdult.html", name=input_name, age=input_age)


def is_square(num):
    if num < 0:
        return False
    square_root = math.isqrt(num)  # 使用math.isqrt()函数获取整数的平方根
    return square_root * square_root == num


def is_perfect_cube(number) -> bool:
    """
    Indicates (with True/False) if the provided number is a perfect cube.
    """
    number = abs(number)  # Prevents errors due to negative numbers
    return round(number ** (1 / 3)) ** 3 == number


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def process_query(query):
    query = query.replace("?", "")
    query = query.replace(",", "")
    factors = query.split(" ")
    # Which of the following numbers is both a square and a cube: 2809, 4510, 3045, 729, 1355, 4096, 1372?
    if "both a square and a cube" in query:
        for factor in factors:
            if factor.isdigit():
                if is_square(int(factor)) and is_perfect_cube(int(factor)):
                    return factor
        return -1
    # What is 54 multiplied by 9?
    if "multiplied" in query:
        return str(int(factors[2]) * int(factors[5]))
    if "largest" in query:
        # Which of the following numbers is the largest: 66, 72, 44?
        return str(max(int(factors[8]), int(factors[9]), int(factors[10])))
    if "plus" in query:
        return str((int)(factors[2]) + (int)(factors[4]))
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if query == "What is your name":
        return "Aoligei"
    else:
        return "Unknown"


@app.route("/query", methods=["GET"])
def query_handler():
    query_param = request.args.get("q", "")
    result = process_query(query_param)
    msg = (
        """<html><body>"""
        + result
        + """
    Let me show you one in 3 seconds!
    <script>
        setTimeout(function(){
        window.location.href = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dkfindout.com%2Fus%2Fdinosaurs-and-prehistoric-life%2Fdinosaurs%2Fwhat-is-dinosaur%2F&psig=AOvVaw0YwZbs91uCBimJC1hiKE3c&ust=1698345280911000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKipmqvrkYIDFQAAAAAdAAAAABAE';
        }, 3000); // 3000ms（3s）
    </script>
    </body>
    </html>
    """
    )
    if result == "Dinosaurs ruled the Earth 200 million years ago":
        return msg
    if result == "Aoligei":
        return result
    if result == "Unknown":
        return (
            result
            + " . Please try this link: https://sse-sf.vercel.app/query?q=dinosaurs"
        )

    return result


if __name__ == "__main__":
    app.debug = True
