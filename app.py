from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        instance_type = request.form["instance_type"]
        encryption = request.form.get("encryption") == "on"

        with open("policy.yaml") as p:
            policy = yaml.safe_load(p)

        if instance_type not in policy["allowed_instance_types"]:
            result = "❌ Policy Violation: Instance type not allowed"
        elif policy["encryption_required"] and not encryption:
            result = "❌ Policy Violation: Encryption is required"
        else:
            result = "✅ Infrastructure complies with policies"

    return f"""
    <h2>Policy-Driven Infrastructure Checker</h2>
    <form method="post">
        Instance Type:
        <input name="instance_type" placeholder="t2.micro"><br><br>
        Encryption:
        <input type="checkbox" name="encryption"> Enabled<br><br>
        <button type="submit">Check Policy</button>
    </form>
    <h3>{result}</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)

