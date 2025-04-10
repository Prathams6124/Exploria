from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required
from cache import LRUCache
from utils import binomial_rand, expensive_function, record_latency
from auth import auth_bp
import time

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
cache = LRUCache()

@app.route("/compute", methods=["GET"])
@jwt_required()
def compute():
    input_value = binomial_rand()
    
    start_time = time.time()
    result, status = cache.get(input_value)
    
    if not result:
        result = expensive_function(input_value)
        cache.put(input_value, result)
    
    latency = time.time() - start_time
    record_latency(latency)

    return jsonify({
        "input": input_value,
        "result": result,
        "latency": latency,
        "cache": status
    })

if __name__ == "__main__":
    app.run(debug=True)
