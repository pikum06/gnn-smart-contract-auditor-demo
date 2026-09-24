import os
import re

# Advanced Detection Patterns
# These look for dangerous combinations, not just words.
VULNERABILITY_PATTERNS = {
    "UNPROTECTED_SELFDESTRUCT": {
        "regex": r"selfdestruct\s*\(",
        "weight": 40,
        "description": "Critical: Code allows contract destruction."
    },
    "HIDDEN_MINT": {
        "regex": r"function\s+\w*mint\w*\s*\(",
        "weight": 25,
        "description": "High: Potential for infinite token printing."
    },
    "OWNER_CENTRALIZATION": {
        "regex": r"onlyOwner|require\s*\(msg\.sender\s*==\s*owner",
        "weight": 10,
        "description": "Medium: High level of centralized control."
    },
    "EXTERNAL_CALLS": {
        "regex": r"\.call\{|delegatecall",
        "weight": 20,
        "description": "Medium: Possible re-entrancy or logic hijacking."
    }
}

def analyze_contract(file_name):
    if not os.path.exists(file_name):
        return None, ["File not found"]
    
    with open(file_name, 'r') as file:
        content = file.read()
        
    score = 100
    findings = []
    
    for key, data in VULNERABILITY_PATTERNS.items():
        # Using case-insensitive search for flexibility
        matches = re.findall(data["regex"], content, re.IGNORECASE)
        if matches:
            score -= data["weight"]
            findings.append(f"{data['description']} (Matches found: {len(matches)})")
            
    return max(0, score), findings

if __name__ == "__main__":
    target = "malicious_sample.sol"
    print(f"CONDUCTING ADVANCED AUDIT: {target}")
    
    score, logs = analyze_contract(target)
    print(f"ULTIMATE SAFETY SCORE: {score}/100")
    print("LOGS:")
    for log in logs:
        print(f" >> {log}")