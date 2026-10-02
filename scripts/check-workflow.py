"""校验主页的 GitHub Actions 工作流结构"""
import yaml

with open(".github/workflows/pages.yml", encoding="utf-8") as f:
    d = yaml.safe_load(f)

print("YAML 解析成功")
print("触发条件 :", list(d[True].keys()) if True in d else list(d["on"].keys()))
print("权限     :", d["permissions"])
print("并发组   :", d["concurrency"]["group"])
for job, cfg in d["jobs"].items():
    env = cfg.get("environment")
    env_name = env.get("name") if isinstance(env, dict) else env
    print(f"\n[job] {job}  needs={cfg.get('needs', '-')}  environment={env_name or '-'}")
    for s in cfg["steps"]:
        label = s.get("name") or s.get("uses")
        extra = ""
        if s.get("with"):
            extra = " " + str(s["with"])
        print(f"   - {label}{extra}")
