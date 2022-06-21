from models import Module
m = Module.objects.latest("id").id
print(m)
l = f"module/7/content/Moduł1/create/"