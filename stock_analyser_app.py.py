from utility_functions import *
from flask import Flask,request,redirect,url_for,render_template,jsonify

app=Flask(__name__)
@app.route("/main_page",methods=["POST"])

def inputurl():
    if request.method=="POST":

        try :
            url=request.form["url"]

            score = str(get_score(url))

            rating, info, lst_yr_info = get_company_details_and_rating(url)

            ls_price = lst_yr_info[0]
            curr_price = lst_yr_info[1]
            gain = lst_yr_info[2]
            
            return render_template("analyse_stock.html",score = score, rating = rating, info = info,
                               ls_price = ls_price, curr_price = curr_price, gain = gain)

        except UnboundLocalError:
            return render_template("error.html", msg = "Our algorithm couldn't get the analyse this stock. Make sure the company-stock is not of any kind of bank's, as banks are currently not supported.")

        except IndexError:
            return render_template("error.html", msg = "Invalid url. Make sure to enter a valid url. See the project description on how to get the valid url")
        
    else:
        print("Wrong url")
if __name__=="__main__":
    app.run(debug=True)
