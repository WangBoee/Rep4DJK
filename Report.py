import os
import time
import json
import requests
import platform

"""
format of each user:
"{id}": {"name": "{name}","morn": 0,"noon": 0,"time": "{datetime}"}
example:
"99999": {"name": "Boi","morn": 0,"noon": 0,"time": "2020-01-01"}
"""

# Report URL
url = 'https://gkdapp.strongmap.cn:9045/api/healthReportDd/add'
# POST header
hd = {
	'Connection': 'keep-alive',
	'Content-Length': '3813',
	'Accept': 'application/json, text/plain, */*',
	'Authorization': 'xxxxxx',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
	'XZT-CLIENTID': 'PC-001',
	'content-type': 'application/json;charset=UTF-8',
	'Referer': 'https://servicewechat.com/wxe9c88300c9903b6d/55/page-frame.html',
	'Accept-Encoding': 'gzip, deflate, br',
}

# POST JSON data of morning(Dict in Python)
body_of_morning = {
	"id": None,
	"reportNodeId": "195",
	"userId": 0,
	"type": 1,
	"healthState": "",
	"isBadSymptoms": False,
	"isTouchill": None,
	"isStayortouch": None,
	"temperature": None,
	"atProvince": "广西壮族自治区",
	"atCity": "柳州市",
	"atDistrict": "城中区",
	"isHospitalize": None,
	"isHeat": None,
	"illSymptom": "",
	"otherIllSymptom": None,
	"hospital": "",
	"diagnosisDisease": "",
	"illState": "",
	"userLocation": "1",
	"caseTreatReportId": None,
	"treatTime": None,
	"isBackSchool": None,
	"backSchoolTime": None,
	"isAbsenceFromDuty": False,
	"leaveRecordId": None,
	"abroadLocation": None,
	"schoolId": 790,
	"tmplFieldList": [
		{
			"id": 124,
			"fieldName": "是否接触疑似或确诊的新型肺炎患者",
			"fieldContent": "false",
			"fieldType": 3,
			"dictName": None,
			"typeId": 19,
			"fatherId": 0,
			"fatherValue": None,
			"level": 1,
			"displaySort": 1,
			"createTime": 1590713460000,
			"updateTime": 1590713460000,
			"createBy": "胡耀文",
			"updateBy": "胡耀文",
			"children": [
				{
					"id": 126,
					"fieldName": "是否医学隔离",
					"fieldContent": None,
					"fieldType": 3,
					"dictName": None,
					"typeId": 19,
					"fatherId": 124,
					"fatherValue": "true",
					"level": 2,
					"displaySort": 1,
					"createTime": 1590713503000,
					"updateTime": 1590713503000,
					"createBy": "胡耀文",
					"updateBy": "胡耀文",
					"children": [
						{
							"id": 127,
							"fieldName": "隔离地址",
							"fieldContent": None,
							"fieldType": 1,
							"dictName": None,
							"typeId": 19,
							"fatherId": 126,
							"fatherValue": "true",
							"level": 3,
							"displaySort": 1,
							"createTime": 1590713520000,
							"updateTime": 1590713520000,
							"createBy": "胡耀文",
							"updateBy": "胡耀文",
							"label": "隔离地址",
							"hasChildren": False
						},
						{
							"id": 128,
							"fieldName": "隔离方式",
							"fieldContent": None,
							"fieldType": 1,
							"dictName": None,
							"typeId": 19,
							"fatherId": 126,
							"fatherValue": "true",
							"level": 3,
							"displaySort": 2,
							"createTime": 1590713538000,
							"updateTime": 1590713538000,
							"createBy": "胡耀文",
							"updateBy": "胡耀文",
							"label": "隔离方式",
							"hasChildren": False
						}
					],
					"label": "是否医学隔离",
					"hasChildren": True
				}
			],
			"label": "是否接触疑似或确诊的新型肺炎患者",
			"hasChildren": True
		},
		{
			"id": 125,
			"fieldName": "是否因新冠肺炎就诊住院",
			"fieldContent": "false",
			"fieldType": 3,
			"dictName": None,
			"typeId": 19,
			"fatherId": 0,
			"fatherValue": None,
			"level": 1,
			"displaySort": 2,
			"createTime": 1590713481000,
			"updateTime": 1590713481000,
			"createBy": "胡耀文",
			"updateBy": "胡耀文",
			"children": [
				{
					"id": 129,
					"fieldName": "医院位置",
					"fieldContent": None,
					"fieldType": 1,
					"dictName": None,
					"typeId": 19,
					"fatherId": 125,
					"fatherValue": "true",
					"level": 2,
					"displaySort": 1,
					"createTime": 1590713581000,
					"updateTime": 1590713581000,
					"createBy": "胡耀文",
					"updateBy": "胡耀文",
					"label": "医院位置",
					"hasChildren": False
				},
				{
					"id": 130,
					"fieldName": "确诊/诊断日期",
					"fieldContent": None,
					"fieldType": 4,
					"dictName": None,
					"typeId": 19,
					"fatherId": 125,
					"fatherValue": "true",
					"level": 2,
					"displaySort": 2,
					"createTime": 1590713599000,
					"updateTime": 1590713599000,
					"createBy": "胡耀文",
					"updateBy": "胡耀文",
					"label": "确诊/诊断日期",
					"hasChildren": False
				},
				{
					"id": 131,
					"fieldName": "是否医学隔离",
					"fieldContent": None,
					"fieldType": 3,
					"dictName": None,
					"typeId": 19,
					"fatherId": 125,
					"fatherValue": "true",
					"level": 2,
					"displaySort": 3,
					"createTime": 1590713616000,
					"updateTime": 1590713616000,
					"createBy": "胡耀文",
					"updateBy": "胡耀文",
					"children": [
						{
							"id": 132,
							"fieldName": "隔离地址",
							"fieldContent": None,
							"fieldType": 1,
							"dictName": None,
							"typeId": 19,
							"fatherId": 131,
							"fatherValue": "true",
							"level": 3,
							"displaySort": 1,
							"createTime": 1590713630000,
							"updateTime": 1590713630000,
							"createBy": "胡耀文",
							"updateBy": "胡耀文",
							"label": "隔离地址",
							"hasChildren": False
						},
						{
							"id": 133,
							"fieldName": "隔离方式",
							"fieldContent": None,
							"fieldType": 1,
							"dictName": None,
							"typeId": 19,
							"fatherId": 131,
							"fatherValue": "true",
							"level": 3,
							"displaySort": 2,
							"createTime": 1590713642000,
							"updateTime": 1590713642000,
							"createBy": "胡耀文",
							"updateBy": "胡耀文",
							"label": "隔离方式",
							"hasChildren": False
						}
					],
					"label": "是否医学隔离",
					"hasChildren": True
				}
			],
			"label": "是否因新冠肺炎就诊住院",
			"hasChildren": True
		}
	]
}

# POST JSON data of afternoon(Dict in Python)
body_of_afternoon = {
	"id": None,
	"reportNodeId": "196",
	"userId": 27694,
	"type": 1,
	"healthState": "",
	"isBadSymptoms": False,
	"isTouchill": None,
	"isStayortouch": None,
	"temperature": None,
	"atProvince": "广西壮族自治区",
	"atCity": "柳州市",
	"atDistrict": "城中区",
	"isHospitalize": None,
	"isHeat": None,
	"illSymptom": "",
	"otherIllSymptom": None,
	"hospital": "",
	"diagnosisDisease": "",
	"illState": "",
	"userLocation": "1",
	"caseTreatReportId": None,
	"treatTime": None,
	"isBackSchool": None,
	"backSchoolTime": None,
	"isAbsenceFromDuty": None,
	"leaveRecordId": None,
	"abroadLocation": None,
	"schoolId": 790,
	"tmplFieldList": [
		{
			"id": 134,
			"fieldName": "学习状态",
			"fieldContent": "非常良好",
			"fieldType": 2,
			"dictName": "common_status",
			"typeId": 20,
			"fatherId": 0,
			"fatherValue": None,
			"level": 1,
			"displaySort": 1,
			"createTime": 1590713788000,
			"updateTime": 1590713788000,
			"createBy": "胡耀文",
			"updateBy": "胡耀文",
			"label": "学习状态",
			"hasChildren": False
		},
		{
			"id": 135,
			"fieldName": "生活状态",
			"fieldContent": "非常良好",
			"fieldType": 2,
			"dictName": "common_status",
			"typeId": 20,
			"fatherId": 0,
			"fatherValue": None,
			"level": 1,
			"displaySort": 2,
			"createTime": 1590713799000,
			"updateTime": 1590713799000,
			"createBy": "胡耀文",
			"updateBy": "胡耀文",
			"label": "生活状态",
			"hasChildren": False
		},
		{
			"id": 136,
			"fieldName": "交际状态",
			"fieldContent": "非常良好",
			"fieldType": 2,
			"dictName": "common_status",
			"typeId": 20,
			"fatherId": 0,
			"fatherValue": None,
			"level": 1,
			"displaySort": 3,
			"createTime": 1590713812000,
			"updateTime": 1590713812000,
			"createBy": "胡耀文",
			"updateBy": "胡耀文",
			"label": "交际状态",
			"hasChildren": False
		},
		{
			"id": 137,
			"fieldName": "情感状态",
			"fieldContent": "非常良好",
			"fieldType": 2,
			"dictName": "common_status",
			"typeId": 20,
			"fatherId": 0,
			"fatherValue": None,
			"level": 1,
			"displaySort": 4,
			"createTime": 1590713821000,
			"updateTime": 1590713821000,
			"createBy": "胡耀文",
			"updateBy": "胡耀文",
			"label": "情感状态",
			"hasChildren": False
		},
		{
			"id": 138,
			"fieldName": "身体状态",
			"fieldContent": "非常良好",
			"fieldType": 2,
			"dictName": "common_status",
			"typeId": 20,
			"fatherId": 0,
			"fatherValue": None,
			"level": 1,
			"displaySort": 5,
			"createTime": 1590713831000,
			"updateTime": 1590713831000,
			"createBy": "胡耀文",
			"updateBy": "胡耀文",
			"label": "身体状态",
			"hasChildren": False
		}
	]
}


def read_file(t_file):
	# open file and read token
	f = open(t_file, 'r')
	str_in = f.read()
	# add token to headers
	hd['Authorization'] = str_in
	# test
	print("#test:str = " + str_in)
	f.close()
	# test
	print('\n', hd, '\n')


# save response to file
def fileout(r_txt, l_file):
	l_file = l_file + '-' + time.strftime("%Y-%m-%d", time.localtime()) + '.log'
	fo = open(l_file, 'ab+')
	# log time
	time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	r_txt = '[' + time_str + ']\n' + r_txt + '\n\n'
	fo.write(r_txt.encode('utf-8'))
	fo.close()


def save_user_list(ot):
	for u in ot:
		ot[u]['time'] = time.strftime("%Y-%m-%d", time.localtime())
	with open('userData.json', 'w', encoding = 'utf-8') as fp:
		dat = json.dumps(ot, ensure_ascii = False, indent = 4)  # .encode('utf-8')
		fp.write(dat)


def load_user_list():
	with open('userData.json', 'r', encoding = 'utf-8') as fp:
		dt = fp.read()
		dat = json.loads(dt)
		print(dat, type(dat))

	now = time.strftime("%Y-%m-%d", time.localtime())
	for u in dat:
		if dat[u]['time'] != now:
			dat[u]['morn'] = 0
			dat[u]['noon'] = 0
	return dat


def check_platform():
	pf = 1  # flag, 1: Windows, 0: Linux
	l_file = './out'  # path of log file
	t_file = './token.txt'  # path of token file
	if platform.system() == 'Windows':  # Windows
		pf = 1	
	elif platform.system() == 'Linux':  # Linux(WSL)
		pf = 0
	else:
		print('Unsupported Platform!')
		exit(0)
	print('Platform: ' + platform.system() + '\tFile path: ' + l_file)
	fileout('Platform: ' + platform.system() + '\tFile path: ' + l_file, l_file)
	return l_file, t_file, pf  # return file path and flag


def rep(user_list, userid, rep_data, node = ''):
	str_out = ''  # log info
	# POST for report
	report = requests.post(url, data = rep_data, headers = hd)
	# check response code, success:201, auth failed:400
	if report.status_code == 201:
		user_list[userid][node] = 1
		print('success\ncode:', report.status_code)
	else:
		print('error\ncode:', report.status_code)
	print('\nresponse body:', report.text)
	str_out = 'Report Node: ' + node + '\nUserId: ' + str(userid) + '\nName:' + userList[userid][
		'name'] + '\nResponse_Info: ' + report.text
	return str_out


def report_all(user_list, l_file):
	for userid in user_list:
		str_out = 'Already Reported'
		# change userId
		body_of_morning["userId"] = int(userid)
		body_of_afternoon["userId"] = int(userid)

		# userid to str, for fileout (alpha ver.)
		# userid_str = str(userid)

		# transform python dict format to JSON format
		# must encode in UTF-8 or it will cause JsonParseException
		body_morning = json.dumps(body_of_morning).encode('utf-8')
		body_afternoon = json.dumps(body_of_afternoon).encode('utf-8')
		# rep_data = body_morning
		# debug info
		print(f"ID:{userid}\nName:{userList[userid]['name']}")
		# print(body_of_morning, '\n')
		# print(body_morning, '\n')
		now = time.strftime("%Y-%m-%d", time.localtime())

		if user_list[userid]["time"] != now:
			if user_list[userid]['morn'] == 0:
				str_out = rep(user_list, userid, body_morning, 'morn')

			# check time, continue if time < 12
			if time.localtime().tm_hour < 12:
				continue

			if user_list[userid]['noon'] == 0:
				# 1s delay for noon report
				time.sleep(1)
				str_out = rep(user_list, userid, body_afternoon, 'noon')
			# 2s delay for next user report
			time.sleep(2)
		else:
			if user_list[userid]['morn'] == 0:
				str_out = rep(user_list, userid, body_morning, 'morn')
			if user_list[userid]['noon'] == 0:
				str_out = rep(user_list, userid, body_afternoon, 'noon')

		print(str_out)
		fileout(str_out, l_file)



if __name__ == "__main__":
	userList = load_user_list()
	# check platform, get path of log file and token file
	log_file, token_file, flag = check_platform()
	read_file(tk_file)  # read token from token.txt
	time.sleep(3)
	print(log_file, '\t', token_file, '\t', flag)
	report_all(userList, log_file)
	save_user_list(userList)
