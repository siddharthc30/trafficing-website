from flask import Flask, render_template, redirect, request, flash, url_for
import random
import os
from plots import *


app = Flask(__name__)
app.secret_key = "hello"
prob = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=["POST", "GET"])
def compute():
    global prob
    if request.method == "POST":
        prob.append(request.form["a"])
        prob.append(request.form["b"])
        prob.append(request.form["c"])
        prob.append(request.form["d"])
        prob.append(request.form["e"])
        prob.append(request.form["f"])
        prob.append(request.form["g"])
        prob.append(request.form["h"])
        prob.append(request.form["i"])
        prob.append(request.form["j"])
        prob.append(request.form["k"])
        prob.append(request.form["l"])
        prob.append(request.form["m"])
        prob.append(request.form["n"])
        prob.append(request.form["o"])
        prob.append(request.form["p"])

        prob = list(map(float, prob))
        if prob[0] + prob[1] + prob[2] != 1:
            flash("The probabilities need to be summed to 1", "info")

        if prob[3] + prob[4] + prob[5] + prob[6] != 1:
            flash("The probabilities need to be summed to 1", "info")

        if prob[7] + prob[8] + prob[9] != 1:
            flash("The probabilities need to be summed to 1", "info")

        if prob[10] + prob[11] != 1:
            flash("The probabilities need to be summed to 1", "info")

        if prob[12] + prob[13] + prob[14] != 1:
            flash("The probabilities need to be summed to 1", "info")

        if prob[15] != 1:
            flash("The value of P must be 1 only", "info")

        else:
            return redirect(url_for("plots"))
            

@app.route('/plots')
def plots():
    time_arr = []
    total_time_arr = []
    time_gp = -1/(prob[0] - 1)
    time_arr.append(time_gp)
    time_previct = time_gp
    total_time_arr.append(time_previct)

    time_rec = -prob[1]/(prob[0]+prob[3]-prob[0]*prob[3]-1)
    time_arr.append(time_rec)
    time_te = -(prob[1]*prob[4]+prob[1]*prob[5]*prob[10]-prob[1]*prob[4]*prob[13]-prob[1]*prob[5]*prob[10]*prob[13]+prob[1]*prob[5]*prob[11]*prob[12])/(prob[0]+prob[3]+prob[7]+prob[13]-prob[0]*prob[3]-prob[0]*prob[7]-prob[3]*prob[7]-prob[0]*prob[13]-prob[3]*prob[13]+prob[8]*prob[10]-prob[7]*prob[13]+prob[0]*prob[3]*prob[7]+prob[0]*prob[3]*prob[13]-prob[0]*prob[8]*prob[10]+prob[0]*prob[7]*prob[13]-prob[3]*prob[8]*prob[10]+prob[3]*prob[7]*prob[13]-prob[8]*prob[10]*prob[13]+prob[8]*prob[11]*prob[12]+prob[0]*prob[3]*prob[8]*prob[10]-prob[0]*prob[3]*prob[7]*prob[13]+prob[0]*prob[8]*prob[10]*prob[13]-prob[0]*prob[8]*prob[11]*prob[12]+prob[3]*prob[8]*prob[10]*prob[13]-prob[3]*prob[8]*prob[11]*prob[12]-prob[0]*prob[3]*prob[8]*prob[10]*prob[13]+prob[0]*prob[3]*prob[8]*prob[11]*prob[12]-1)
    time_arr.append(time_te)
    time_vict = time_rec + time_te
    total_time_arr.append(time_vict)

    time_inter = -(prob[1]*prob[5]-prob[1]*prob[5]*prob[7]+prob[1]*prob[4]*prob[8]-prob[1]*prob[5]*prob[13]+prob[1]*prob[5]*prob[7]*prob[13]-prob[1]*prob[4]*prob[8]*prob[13])/(prob[0]+prob[3]+prob[7]+prob[13]-prob[0]*prob[3]-prob[0]*prob[7]-prob[3]*prob[7]-prob[0]*prob[13]-prob[3]*prob[13]+prob[8]*prob[10]-prob[7]*prob[13]+prob[0]*prob[3]*prob[7]+prob[0]*prob[3]*prob[13]-prob[0]*prob[8]*prob[10]+prob[0]*prob[7]*prob[13]-prob[3]*prob[8]*prob[10]+prob[3]*prob[7]*prob[13]-prob[8]*prob[10]*prob[13]+prob[8]*prob[11]*prob[12]+prob[0]*prob[3]*prob[8]*prob[10]-prob[0]*prob[3]*prob[7]*prob[13]+prob[0]*prob[8]*prob[10]*prob[13]-prob[0]*prob[8]*prob[11]*prob[12]+prob[3]*prob[8]*prob[10]*prob[13]-prob[3]*prob[8]*prob[11]*prob[12]-prob[0]*prob[3]*prob[8]*prob[10]*prob[13]+prob[0]*prob[3]*prob[8]*prob[11]*prob[12]-1)
    time_arr.append(time_inter)
    time_surv = -(prob[1]*prob[5]*prob[11]-prob[1]*prob[5]*prob[7]*prob[11]+prob[1]*prob[4]*prob[8]*prob[11])/(prob[0]+prob[3]+prob[7]+prob[13]-prob[0]*prob[3]-prob[0]*prob[7]-prob[3]*prob[7]-prob[0]*prob[13]-prob[3]*prob[13]+prob[8]*prob[10]-prob[7]*prob[13]+prob[0]*prob[3]*prob[7]+prob[0]*prob[3]*prob[13]-prob[0]*prob[8]*prob[10]+prob[0]*prob[7]*prob[13]-prob[3]*prob[8]*prob[10]+prob[3]*prob[7]*prob[13]-prob[8]*prob[10]*prob[13]+prob[8]*prob[11]*prob[12]+prob[0]*prob[3]*prob[8]*prob[10]-prob[0]*prob[3]*prob[7]*prob[13]+prob[0]*prob[8]*prob[10]*prob[13]-prob[0]*prob[8]*prob[11]*prob[12]+prob[3]*prob[8]*prob[10]*prob[13]-prob[3]*prob[8]*prob[11]*prob[12]-prob[0]*prob[3]*prob[8]*prob[10]*prob[13]+prob[0]*prob[3]*prob[8]*prob[11]*prob[12]-1)
    time_arr.append(time_surv)
    time_postvict = time_inter + time_surv
    total_time_arr.append(time_postvict)

    time_arr = [k/12 for k in time_arr]
    total_time_arr = [t/12 for t in total_time_arr]

    x = plot_state_time(time_arr)
    y = plot_stage_time(total_time_arr)

    return render_template("plots.html", state_time = x, stage_time = y)
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(debug = True)