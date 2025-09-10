#!/usr/bin/env python3
"""
Verification script for ai-plugin.json configuration files.
This script validates the ChatGPT Actions plugin configuration.
"""

import json
import sys
from pathlib import Path

def validate_ai_plugin_config(file_path: str) -> bool:
    """Validate an ai-plugin.json configuration file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Required fields for ChatGPT Actions
        required_fields = [
            'schema_version',
            'name_for_human',
            'name_for_model',
            'description_for_human',
            'description_for_model',
            'auth',
            'api'
        ]
        
        missing_fields = []
        for field in required_fields:
            if field not in config:
                missing_fields.append(field)
        
        if missing_fields:
            print(f"❌ Missing required fields in {file_path}: {', '.join(missing_fields)}")
            return False
        
        # Validate auth configuration
        auth_type = config['auth']['type']
        if auth_type not in ['api_key', 'service_http']:
            print(f"❌ Invalid auth type in {file_path}: expected 'api_key' or 'service_http', got '{auth_type}'")
            return False
        
        # For service_http auth, check for required fields
        if auth_type == 'service_http':
            if 'authorization_type' not in config['auth']:
                print(f"❌ Missing 'authorization_type' in service_http auth for {file_path}")
                return False
            if 'verification_tokens' not in config['auth']:
                print(f"❌ Missing 'verification_tokens' in service_http auth for {file_path}")
                return False
        
        # Validate API configuration
        if config['api']['type'] != 'openapi':
            print(f"❌ Invalid API type in {file_path}: expected 'openapi', got '{config['api']['type']}'")
            return False
        
        if not config['api'].get('is_user_authenticated'):
            print(f"❌ API should be user authenticated in {file_path}")
            return False
        
        print(f"✅ {file_path} is valid")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in {file_path}: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return False
    except Exception as e:
        print(f"❌ Error validating {file_path}: {e}")
        return False

def main():
    """Main verification function."""
    print("🔍 Verifying ChatGPT Actions plugin configuration...")
    print()
    
    # Check both ai-plugin.json files
    config_files = [
        'ai-plugin.json',
        '.well-known/ai-plugin.json'
    ]
    
    all_valid = True
    
    for config_file in config_files:
        if Path(config_file).exists():
            if not validate_ai_plugin_config(config_file):
                all_valid = False
        else:
            print(f"❌ Configuration file not found: {config_file}")
            all_valid = False
    
    print()
    if all_valid:
        print("🎉 All ChatGPT Actions plugin configurations are valid!")
        print("✅ Ready for deployment to ChatGPT Actions")
    else:
        print("❌ Some configuration files have issues that need to be fixed")
        sys.exit(1)

if __name__ == '__main__':
    main()
