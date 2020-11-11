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

    def _verify(self):
        pass

    def _attack(self):
        pass

    def run(self, **kwargs):
        if self.mode == 'verify':
            return self._verify(**kwargs)
        elif self.mode == 'attack':
            return self._attack(**kwargs)


class OutPut(object):

    def __init__(self, poc_object=None):
        if poc_object:
            self.pid = poc_object.pid
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
            "status": "success",
            "result": result
        }

        # SUCCESS_COUNT =  SUCCESS_COUNT + 1

        RESULT.append(tmp_result)
        msg = "{} {} [{}] is vulnerable".format(self.mode, self.target, self.name)
        lightcyan(msg)

    def fail(self, error=""):
        # 失败调用这里
        tmp_result = {
            "target": self.target,
            "name": self.name,
            "app_name": self.app_name,
            "app_version": self.app_version,
            "mode": self.mode,
            "status": "failed",
            "result": {"extra": str(error)},
        }
        # 放到 data 中的 RESULT
        RESULT.append(tmp_result)
        msg = "{} {} [{}] failed: {}".format(self.mode, self.target, self.name, error)
        yellow(msg)

