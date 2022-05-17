import importlib
import inspect

g_ModuleCache = {}

# 指定したPathのモジュールを取得します。
def GetModule(modulePath):
    if modulePath in g_ModuleCache:
        # 既に読み込んでいたらreload
        g_ModuleCache[modulePath] = importlib.reload(g_ModuleCache[modulePath])
        print('Module: ' + modulePath + ' reloaded.')
    else:
        g_ModuleCache[modulePath] = importlib.import_module(modulePath)
        print('Module: ' + modulePath + ' loaded.')
    return g_ModuleCache[modulePath]

# 指定したPathモジュール内に存在する、以下の条件を満たしている最初に見つかったクラスを返します。
# ・typeを継承している
# ・NAME属性を持つ
# 存在しない場合Noneを返します。
def TryGetNamedClass(modulePath, type):
    module = GetModule(modulePath)
    classes = inspect.getmembers(module, inspect.isclass)
    for cls in classes:
        c = cls[1]
        if issubclass(c, type) and hasattr(c, 'NAME') and c.NAME:
            return c
    return None
