ATTACKS = { # List of possible attacks and the monetary value an inverter company may lose if hit by the attack
    "Brute force on credentials": 426, # https://www.ibm.com/reports/data-breach
    "Credential stuffing": 481, # https://www.ibm.com/reports/data-breach
    "Man-in-the-Middle": 426, # https://www.ibm.com/reports/data-breach
    "Session replay": 100, # https://www.packetlabs.net/posts/a-guide-to-replay-attacks-and-how-to-defend-against-them/
    "Lateral movement within systems": 28, # https://fidelissecurity.com/cybersecurity-101/learn/lateral-movement/
    "Reconnaissance": 445, # https://www.sentinelone.com/cybersecurity-101/cybersecurity/cyber-security-statistics/
    "Unauthorized port/service access": 18, # https://www.cyber.gov.au/about-us/view-all-content/reports-and-statistics/annual-cyber-threat-report-2023-2024
    "Advanced persistent threats": 426, # https://www.nationaldefensemagazine.org/articles/2024/4/3/viewpoint-containing-rise-of-advanced-persistent-threats
    "Ransomware": 185, # https://www.getastra.com/blog/security-audit/ransomware-attack-statistics/
    "Phishing": 488, # https://hoxhunt.com/guide/phishing-trends-report
    "Distributed Denial of Service": 27 # https://cybermaterial.com/ddos-attacks-cost-6000-per-minute-in-2024/
}

DEFENCES = { # defence methods and implementation levels of possible solutions to strengthen inverters
    "Authentication and Access Controls": { # addition/upgrade of methods used to control user access and movement in a system (Low Level)
        "levels": {
            1: {
                "cost": 50,
                "description": "Default passwords changed and introduction of basic user roles.",
                "mitigates": [
                    "Brute force on credentials"
                ]
            },
            2: {
                "cost": 200,
                "description": "Strong password policies and account management.",
                "mitigates": [
                    "Brute force on credentials",
                    "Credential stuffing"
                ]
            },
            3: {
                "cost": 500,
                "description": "Role-based access controls.",
                "mitigates": [
                    "Brute force on credentials",
                    "Credential stuffing",
                    "Lateral movement within systems"
                ]
            },
            4: {
                "cost": 1200,
                "description": "Multi-factor authentication.",
                "mitigates": [
                    "Brute force on credentials",
                    "Credential stuffing",
                    "Lateral movement within systems",
                    "Phishing"
                ]
            },
            5: {
                "cost": 2000,
                "description": "Centralized identity management such as single sign-on and organisational auditing).",
                "mitigates": [
                    "Brute force on credentials",
                    "Credential stuffing",
                    "Lateral movement within systems",
                    "Phishing",
                    "Ransomware"
                ]
            }
        }
    },
    "Encryption of Communication Protocols": { # addition/upgrade of methods used to secure and encrypt data in transit (Medium Level)
        "levels": {
            1: {
                "cost": 100,
                "description": "Disable plain-text protocols.",
                "mitigates": [
                    "Man-in-the-Middle"
                ]
            },
            2: {
                "cost": 300,
                "description": "Enabling HTTPS and base level TLS",
                "mitigates": [
                    "Man-in-the-Middle",
                    "Session replay"
                ]
            },
            3: {
                "cost": 700,
                "description": "Advanced TLS and introduction of modern ciphers.",
                "mitigates": [
                    "Man-in-the-Middle",
                    "Session replay",
                    "Credential stuffing"
                ]
            },
            4: {
                "cost": 1200,
                "description": "Mutual authentication.",
                "mitigates": [
                    "Man-in-the-Middle",
                    "Session replay",
                    "Credential stuffing",
                    "Phishing attacks"
                ]
            },
            5: {
                "cost": 2000,
                "description": "Zero-trust, continuous certificate validation.",
                "mitigates": [
                    "Man-in-the-Middle",
                    "Session replay",
                    "Credential stuffing",
                    "Phishing attacks",
                    "Advanced persistent threats"
                ]
            }
        }
    },
    "Network Segmentation and Isolation": { # breaking the network into smaller sections, improves efficiency and lowers hacker range (High Level)
        "levels": {
            1: {
                "cost": 150,
                "description": "Logical separation (VLANs).",
                "mitigates": [
                    "Reconnaissance"
                ]
            },
            2: {
                "cost": 400,
                "description": "Physical segmentation.",
                "mitigates": [
                    "Reconnaissance",
                    "Session replay"
                ]
            },
            3: {
                "cost": 800,
                "description": "Firewalls, ACLs.",
                "mitigates": [
                    "Unauthorized port/service access",
                    "Reconnaissance",
                    "Session replay"
                ]
            },
            4: {
                "cost": 1500,
                "description": "DMZ, IDS.",
                "mitigates": [
                    "Unauthorized port/service access",
                    "Reconnaissance",
                    "Session replay",
                    "Distributed Denial of Service"
                ]
            },
            5: {
                "cost": 2200,
                "description": "Micro-segmentation.",
                "mitigates": [
                    "Unauthorized port/service access",
                    "Reconnaissance",
                    "Session replay",
                    "Distributed Denial of Service",
                    "Advanced persistent threats"
                ]
            }
        }
    }
}

LETTER = { # letter abreviasions used to make user input easier
    'A': 'Authentication and Access Controls',
    'E': 'Encryption of Communication Protocols',
    'S': 'Network Segmentation and Isolation'
}

ACRONYM = { # defence method acronyms used to make output easier to show
    'Authentication and Access Controls': 'AAC',
    'Encryption of Communication Protocols': 'ECP',
    'Network Segmentation and Isolation': 'NSI'
}