from flask import Flask, jsonify
from flask import request
import sqlite3

app = Flask(__name__)

sqlite_path = 'excel_check/sqlite'
title = ["人员类别", "员工编号", "人员状态", "姓名", "身份证号码", "出生年月", "年龄", "民族", "性别", "政治面貌", "籍贯", "婚姻状况", "实习类别", "来源分类", "所在部门",
         "部门全称", "入职日期", "司龄", "参加工作时间", "工龄", "岗位序列", "岗位工时", "劳动合同所属公司", "劳动合同起始日期", "劳动合同终止日期", "劳动合同2008年后签订次数",
         "劳动合同类型", "职级类别", "返聘协议起始日期", "返聘协议终止日期", "实习协议起始日期", "实习协议终止日期", "岗位名称", "任职类型", "职称名称", "职称级别", "技能等级",
         "最高学历", "最高学位", "所学专业", "毕业院校", "毕业日期", "电子邮箱", "家庭住址（详细）", "手机号码", "紧急联系人姓名", "紧急联系人电话", "紧急联系人与本人关系",
         "户口所在地", "体检情况", "竞业禁止协议标识", "档案所在地", "档案是否在公司", "长期服务标识", "身份证上地址", "股权激励", "班车", "考勤方式", "社保所属公司", "户口性质",
         "开始缴纳社保日期", "保险缴纳类别", "社保缴费年限", "参加养老标识", "参加公积金标识", "保险代理公司", "公积金个人编号", "社保基数", "公积金基数", "险种缴纳地", "薪资所属公司",
         "工资归属部门", "工资一级部门", "工资二级部门", "工资三级部门", "银行名称", "开户行名称", "工资账号", "参与考核", "所属工资套", "哺乳补贴开始日期", "哺乳补贴结束日期",
         "加班预存标识", "加班小时上限", "综合工时预存上限", "离职类别", "离职原因", "最后工作日", "提前转正期限（月）", "异动类型", "试用期开始日期", "产假开始日期", "产假结束日期",
         "实习转试用日期", "试用期期限（月）", "转正时间", "变动前原职级", "异动日期", "板块名称", "二级部门", "三级部门", "四级部门", "产假应休天数", "已休年假", "哺乳补贴基数",
         "司龄（月）", "原部门", "原岗位名称", "兼任信息", "招聘来源", "招聘类型"]

@app.route('/search/users', methods=["GET"])
def search_users():
    global sql
    name = request.values.get("name")
    job_number = request.values.get("job_number")
    ID_number = request.values.get("ID_number")
    mobile_phone_number = request.values.get("mobile_phone_number")
    conn = sqlite3.connect(sqlite_path)
    cur = conn.cursor()
    if name is not None:
        sql = "select * from staff_info where name=('%s')" % name
    elif job_number is not None:
        sql = "select * from staff_info where job_number=" + job_number
    elif ID_number is not None:
        sql = "select * from staff_info where ID_number=" + ID_number
    elif mobile_phone_number is not None:
        sql = 'select * from staff_info where mobile_phone_number=' + mobile_phone_number
    cur.execute(sql)
    result = cur.fetchall()
    new_result = []
    for i in result:
        # print(list(i))
        dict_result = dict(zip(title, list(i)))
        # print(dict_result)
        new_result.append(dict_result)
    conn.close()
    return jsonify({"code": "00", "data": new_result, "msg": "success"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
