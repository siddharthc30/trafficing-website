import plotly
import plotly.graph_objects as go
import json

def plot_state_time(time_arr):
    labels = ['General Population', 'Recruitment', 'Trafficking-Explotation', 'Intervention', 'Survivor']
    values = [time_arr[0], time_arr[1], time_arr[2], time_arr[3], time_arr[4]]
    fig = go.Figure(go.Bar(x = values, y = labels, orientation='h'))
    fig.update_layout(title_text = "Time (in Years) Individual Spends in Each State")
    state_time_json = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)

    return state_time_json

def plot_stage_time(total_time_arr):
    labels = ['Pre-victimization', 'Victimization', 'Post-victimizattion']
    values = [total_time_arr[0], total_time_arr[1], total_time_arr[2]]
    fig = go.Figure(go.Bar(x = values, y = labels, orientation='h'))
    fig.update_layout(title_text = "Time (in Years) Individual Spends in Each Victimization Stage")
    stage_time_json = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)

    return stage_time_json

