from django.utils.deprecation import MiddlewareMixin

from common.errors import LogicErr
from libs.http import render_json
from common import errors


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 从request.session中获取uid, 如果能获取到,则说明登录.
        # 如果获取不到,表示没登录.
        # 设定可以直接跳过登录检查的地址白名单
        white_list = ['/api/user/submit/phone/',
                      '/api/user/submit/vcode/']
        # print(request.path)
        if request.path in white_list:
            return None

        uid = request.session.get('uid')
        if not uid:
            # 不存在, 说明没登录
            return render_json(code=errors.LOGIN_REQUIRED, data='你好, 请登录')
        # 存在的话,直接把uid写入request
        request.uid = uid


# 捕获逻辑错误异常
class LogicErrMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        # 只捕获逻辑错误异常
        if isinstance(exception, LogicErr):
            # 可以捕获.
            # 直接返回response
            return render_json(code=exception.code, data=exception.data)

