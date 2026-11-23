import ast
import math

import pandas as pd
import streamlit as st

st.title("📈 Graph Plotter")
st.caption("Plot common mathematical functions and explore their behaviour.")

ALLOWED_FUNCTIONS = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
    "exp": math.exp, "abs": abs,
}
ALLOWED_CONSTANTS = {"pi": math.pi, "e": math.e}


def safe_value(node, x_value):
    if isinstance(node, ast.Expression):
        return safe_value(node.body, x_value)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.Name):
        if node.id == "x":
            return x_value
        if node.id in ALLOWED_CONSTANTS:
            return ALLOWED_CONSTANTS[node.id]
        raise ValueError(f"Unknown symbol: {node.id}")
    if isinstance(node, ast.BinOp) and type(node.op) in (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod):
        left = safe_value(node.left, x_value)
        right = safe_value(node.right, x_value)
        if isinstance(node.op, ast.Add): return left + right
        if isinstance(node.op, ast.Sub): return left - right
        if isinstance(node.op, ast.Mult): return left * right
        if isinstance(node.op, ast.Div): return left / right
        if isinstance(node.op, ast.Pow): return left ** right
        return left % right
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = safe_value(node.operand, x_value)
        return value if isinstance(node.op, ast.UAdd) else -value
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ALLOWED_FUNCTIONS and len(node.args) == 1:
        return ALLOWED_FUNCTIONS[node.func.id](safe_value(node.args[0], x_value))
    raise ValueError("Use x, numbers, +, -, *, /, **, parentheses, and supported functions such as sin(x), cos(x), sqrt(x), or log(x).")


function = st.text_input("Enter a function y = ", value="x**2 - 4", help="Examples: x**2, 2*x + 3, sin(x), cos(x), sqrt(x), exp(x)")
left, right = st.columns(2)
with left:
    x_min = st.number_input("Minimum x", value=-10.0, step=1.0)
with right:
    x_max = st.number_input("Maximum x", value=10.0, step=1.0)

if x_min >= x_max:
    st.error("The maximum x must be greater than the minimum x.")
else:
    try:
        expression = ast.parse(function, mode="eval")
        # Validate the expression before evaluating sampled points.
        safe_value(expression, 0.0)
        xs = [x_min + (x_max - x_min) * i / 400 for i in range(401)]
        ys = []
        for xv in xs:
            try:
                yv = float(safe_value(expression, xv))
                ys.append(yv if math.isfinite(yv) and abs(yv) < 1e12 else float("nan"))
            except (ValueError, ZeroDivisionError, OverflowError):
                ys.append(float("nan"))

        valid = [(xv, yv) for xv, yv in zip(xs, ys) if math.isfinite(yv)]
        if not valid:
            st.warning("No finite values were found in this x-range. Try another range or function.")
        else:
            chart_data = pd.DataFrame({"x": [p[0] for p in valid], "y": [p[1] for p in valid]})
            st.line_chart(chart_data, x="x", y="y", height=420)
            st.subheader("Graph analysis")
            y_intercept = safe_value(expression, 0.0)
            a, b, c = st.columns(3)
            a.metric("y-intercept", f"(0, {y_intercept:.4g})")
            b.metric("Sampled minimum", f"{min(p[1] for p in valid):.4g}")
            c.metric("Sampled maximum", f"{max(p[1] for p in valid):.4g}")

            crossings = []
            for (x1, y1), (x2, y2) in zip(valid, valid[1:]):
                if y1 == 0 or y1 * y2 < 0:
                    crossings.append(x1 if y1 == 0 else x1 - y1 * (x2 - x1) / (y2 - y1))
            st.write("**Approximate x-intercepts:** " + (", ".join(f"{v:.4g}" for v in crossings[:12]) if crossings else "None detected in this range"))
            st.caption("Minimum, maximum and intercept values are numerical estimates from sampled points, not symbolic proofs. Trigonometric functions use radians.")
    except (SyntaxError, ValueError, TypeError, ZeroDivisionError, OverflowError) as error:
        st.error(f"Please check the function. {error}")

st.info("Next additions: interactive circuit diagrams, then a robotics simulation lab with a moving robot and adjustable controls.")
