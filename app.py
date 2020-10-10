import os
from flask import Flask, request
import mcelfishapp

app = Flask("McElfish")

HTML = """
<html><body><h1>McElfish</h1>Usage: <a href="?data=20,10,5,1,0">?data=20,10,5,1,0</a> (it might take a minute)</body></html>
"""


def to_data(datastr):
    datastr = datastr.lower().strip()
    if len(datastr) > 3 * 30:
        return []
    allowed = set(" ,0123456789")
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
    mcelfishapp.assert_is_ints(data)
    if not data:
        return HTML

    output = mcelfishapp.get(data)
    if not output:
        return (
            f"<html><body>"
            + f"<p>type={type(output)}</p>"
            + f"<pre>{output}</pre>"
            + f"</body></html>"
        )

    if "html" in output:
        return output

    return f"<html><body><h1>output</h1><pre>{output}</pre></body></html>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host="0.0.0.0", port=port)
