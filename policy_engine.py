import yaml
import json

with open('policy.yaml') as p:
    policy = yaml.safe_load(p)

with open('infrastructure.json') as i:
    infra = json.load(i)

def check_policy(policy, infra):
    if infra["instance_type"] not in policy["allowed_instance_types"]:
        return "❌ Policy Violation: Instance type not allowed"
    if policy["encryption_required"] and not infra["encryption"]:
        return "❌ Policy Violation: Encryption is required"
    return "✅ Infrastructure complies with policies"

print(check_policy(policy, infra))