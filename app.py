from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ----- Serve Frontend -----
@app.route("/")
def index():
    return render_template("index.html")

# ----- API Route -----
@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.get_json()

        # Validate input
        if not data or "data" not in data:
            return jsonify({"is_success": False, "error": "Invalid input"}), 200

        input_array = data["data"]

        # Optional user info
        user_id = data.get("user_id", "john_doe_17091999")
        email = data.get("email", "john@xyz.com")
        roll_number = data.get("roll_number", "ABCD123")

        # ----- Classifications -----
        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0

        for item in input_array:
            if str(item).isdigit():  # numeric
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(item))
                else:
                    odd_numbers.append(str(item))
            elif str(item).isalpha():  # alphabets
                alphabets.append(str(item).upper())
            else:  # special characters
                special_characters.append(str(item))

        # ----- Concat string -----
        all_alpha = "".join(alphabets)
        rev = all_alpha[::-1]
        alt = []
        for i, ch in enumerate(rev):
            alt.append(ch.lower() if i % 2 else ch.upper())
        concat_string = "".join(alt)

        # ----- Response -----
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 200


if __name__ == "__main__":
    app.run(debug=True)
