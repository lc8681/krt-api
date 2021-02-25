from flask import Flask,jsonify


@app.route("/users", methods=["GET"])
def get_users_info():
    """获取所有用户信息"""
    return jsonify({"code":"0", "data":'', "msg":"操作成功"})