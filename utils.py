import random, math, time, json

latencies = []

def binomial_rand():
    u1 = random.random()
    u2 = random.random()
    z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    x = 5 * z + 50
    return int(min(max(1, round(x)), 100))

def expensive_function(input_value):
    time.sleep(2)
    return int(abs(math.sin(input_value) * 1000)) + 1

def record_latency(latency):
    latencies.append(latency)
    if len(latencies) == 1000:
        latencies.sort()
        p90 = latencies[int(0.9 * len(latencies))]
        with open("latency.json", "w") as f:
            json.dump({"P90": p90, "all_latencies": latencies}, f)
