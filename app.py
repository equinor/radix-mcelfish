import os
from flask import Flask, request
import mcelfish

app = Flask("McElfish")

HTML = """
<html><body><h1>McElfish</h1>Usage: <a href="?data=20,10,5,1,0">?data=20,10,5,1,0</a> (it might take a minute)</body></html>
"""


def to_data(datastr):
    datastr = datastr.lower().strip()
    if len(datastr) > 3 * 30:
        return []
    allowed = set(" ,0123456789e+")
    for e in datastr:
        if e not in allowed:
            return []
    datasplit = datastr.split(",")
    data = []
    for i in range(len(datasplit)):
        e = datasplit[i].strip()
        if e:
            try:
                e = int(e)
                data.append(e)
            except:
                return []
    return data


@app.route("/", methods=["GET"])
def main():
    datastr = request.args.get("data")
    if datastr is None:
        return HTML

    data = to_data(datastr)
    if not data:
        return HTML

    model, trace = mcelfish.run(data=data)
    smry, res = mcelfish.summary(model, trace)
    retval = smry.to_html()
    _, _, _, _, beta = mcelfish.beta(res)
    html = f"<div>{retval}</div><p>{beta}</p>"
    return f"<html><body>{html}</body></html>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host="0.0.0.0", port=port)
