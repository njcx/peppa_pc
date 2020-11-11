from peppa_pc.utils import yellow, lightcyan


SUCCESS_COUNT = 0
RESULT = []


class BasePOC(object):

    pid = None            # poc id
    version = None        # poc 版本
    name = None           # poc 名字
    author = None         # poc 作者
    create_date = None    # poc 创建时间
    update_date = None    # poc 更新时间
    app_name = None       # poc 对应的应用名
    app_version = None    # poc 对应的应用版本
    vul_type = None       # poc 类型
    info = None           # 注释

    def __init__(self, target, mode="verify"):
        self.target = target
        self.mode = mode
        self.error = ''

    def verify(self):
        pass

    def attack(self):
        pass

    def run(self, **kwargs):
        if self.mode == 'verify':
            return self.verify(**kwargs)
        elif self.mode == 'attack':
            return self.attack(**kwargs)      # 这里直接调run 函数即可


class OutPut(object):

    def __init__(self, poc_object=None):
        if poc_object:
            self.name = poc_object.name
            self.target = poc_object.target
            self.mode = poc_object.mode
            self.app_name = poc_object.app_name
            self.app_version = poc_object.app_version
            self.vul_type = poc_object.vul_type
            self.info = poc_object.info

    def success(self, result):

        tmp_result = {
            "target": self.target,
            "name": self.name,
            "app_name": self.app_name,
            "app_version": self.app_version,
            "mode": self.mode,
            "vul_type": self.vul_type,
            "info": self.info,
            "status": "success",
            "result": result
        }

        # SUCCESS_COUNT =  SUCCESS_COUNT + 1
        RESULT.append(tmp_result)
        msg = "{} {} [{}] is vulnerable".format(self.mode, self.target, self.name)
        lightcyan(msg)

    def fail(self, error=""):
        tmp_result = {
            "target": self.target,
            "name": self.name,
            "app_name": self.app_name,
            "app_version": self.app_version,
            "mode": self.mode,
            "vul_type": self.vul_type,
            "info": self.info,
            "status": "failed",
            "result": {"extra": str(error)},
        }
        RESULT.append(tmp_result)
        msg = "{} {} [{}] failed: {}".format(self.mode, self.target, self.name, error)
        yellow(msg)

