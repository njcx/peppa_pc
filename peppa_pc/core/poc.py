class BasePOC(object):

    pid = None
    name = None
    author = None
    app = None
    version = None
    v_type = None
    desc = None
    date = None

    def __init__(self):

    def _verify(self):
        pass

    def _attack(self):
        pass

    def run(self,**kwargs):
        if self.mode == 'verify':
            return self._verify(**kwargs)
        elif self.mode == 'attack':
            return self._attack(**kwargs)









class Output(object):
    """
    结果输出
    """
    def __init__(self, poc_info=None):
        if poc_info:
            self.pid = poc_info.pid
            self.name = poc_info.name
            self.target = poc_info.target
            self.mode = poc_info.mode
            self.app = poc_info.app
            self.version = poc_info.version

    def success(self, result):
        # 成功调用这里
        tmp_result = {
            "target": self.target,
            "name": self.name,
            "app": self.app,
            "version": self.version,
            "mode": self.mode,
            "status": "success",
            "result": result
        }
        # 统计成功漏洞数量
        SCAN_RESULT.SUCCESS_COUNT += 1
        # 放到 data 中的 RESULT
        SCAN_RESULT.RESULT.append(tmp_result)
        msg = "{} {} [{}] is vulnerable".format(self.mode.capitalize(), self.target, self.name)
        logger.success(msg)

    def fail(self, error=""):
        # 失败调用这里
        tmp_result = {
            "target": self.target,
            "name": self.name,
            "app": self.app,
            "version": self.version,
            "mode": self.mode,
            "status": "failed",
            "result": {"extra": str(error)},
        }
        # 放到 data 中的 RESULT
        SCAN_RESULT.RESULT.append(tmp_result)
        msg = "{} {} [{}] failed: {}".format(self.mode.capitalize(), self.target, self.name, error)
        logger.warning(msg)
