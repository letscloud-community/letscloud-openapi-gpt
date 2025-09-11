#!/usr/bin/env python3
"""
LetsCloud GPT Actions Configuration Validator

This script validates the ChatGPT Actions configuration files and OpenAPI specification
to ensure they are properly formatted and ready for deployment.

Usage:
    python verify-plugin-config.py
"""

import json
import yaml
import os
import sys
import requests
from pathlib import Path
from typing import Dict, Any, List, Tuple

class ConfigValidator:
    """Validator for LetsCloud GPT Actions configuration."""
    
    def __init__(self, project_root: str = "."):
        """
        Initialize the validator.
        
        Args:
            project_root: Path to the project root directory
        """
        self.project_root = Path(project_root)
        self.errors = []
        self.warnings = []
    
    def validate_openapi_spec(self) -> bool:
        """
        Validate the OpenAPI specification file.
        
        Returns:
            True if valid, False otherwise
        """
        print("🔍 Validating OpenAPI specification...")
        
        openapi_path = self.project_root / "docs" / "openapi.yaml"
        
        if not openapi_path.exists():
            self.errors.append(f"OpenAPI specification not found: {openapi_path}")
            return False
        
        try:
            with open(openapi_path, 'r', encoding='utf-8') as f:
                spec = yaml.safe_load(f)
            
            # Check required fields
            required_fields = ['openapi', 'info', 'paths', 'components']
            for field in required_fields:
                if field not in spec:
                    self.errors.append(f"Missing required field in OpenAPI spec: {field}")
                    return False
            
            # Check OpenAPI version
            if not spec['openapi'].startswith('3.'):
                self.warnings.append(f"OpenAPI version {spec['openapi']} may not be fully supported")
            
            # Check info section
            info_required = ['title', 'description', 'version']
            for field in info_required:
                if field not in spec['info']:
                    self.errors.append(f"Missing required info field: {field}")
            
            # Check paths
            if not spec['paths']:
                self.warnings.append("No API paths defined in OpenAPI spec")
            
            # Check for required endpoints
            required_endpoints = ['/set-apikey', '/proxy']
            for endpoint in required_endpoints:
                if endpoint not in spec['paths']:
                    self.errors.append(f"Missing required endpoint: {endpoint}")
            
            print("✅ OpenAPI specification is valid")
            return True
            
        except yaml.YAMLError as e:
            self.errors.append(f"Invalid YAML in OpenAPI spec: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Error reading OpenAPI spec: {e}")
            return False
    
    
    def validate_file_structure(self) -> bool:
        """
        Validate the project file structure.
        
        Returns:
            True if valid, False otherwise
        """
        print("🔍 Validating project structure...")
        
        required_files = [
            "README.md",
            "LICENSE",
            "docs/openapi.yaml",
            "docs/index.html",
            "docs/_config.yml",
            "examples/usage-examples.py",
            "examples/requirements.txt"
        ]
        
        missing_files = []
        for file_path in required_files:
            full_path = self.project_root / file_path
            if not full_path.exists():
                missing_files.append(file_path)
        
        if missing_files:
            self.errors.append(f"Missing required files: {', '.join(missing_files)}")
            return False
        
        print("✅ Project structure is valid")
        return True
    
    def validate_urls(self) -> bool:
        """
        Validate that referenced URLs are accessible.
        
        Returns:
            True if valid, False otherwise
        """
        print("🔍 Validating referenced URLs...")
        
        # URLs to check
        urls_to_check = [
            "https://letscloud-community.github.io/letscloud-openapi-gpt/docs/openapi.yaml",
            "https://letscloud-community.github.io/letscloud-openapi-gpt/docs/assets/LetsCloud_logo.png",
            "https://letscloud-community.github.io/letscloud-openapi-gpt/privacy-policy.html"
        ]
        
        for url in urls_to_check:
            try:
                response = requests.head(url, timeout=10)
                if response.status_code == 200:
                    print(f"✅ URL accessible: {url}")
                else:
                    self.warnings.append(f"URL returned status {response.status_code}: {url}")
            except requests.exceptions.RequestException as e:
                self.warnings.append(f"URL not accessible: {url} - {e}")
        
        return True
    
    def validate_examples(self) -> bool:
        """
        Validate the Python examples.
        
        Returns:
            True if valid, False otherwise
        """
        print("🔍 Validating Python examples...")
        
        examples_path = self.project_root / "examples" / "usage-examples.py"
        
        if not examples_path.exists():
            self.errors.append("Python examples file not found")
            return False
        
        try:
            with open(examples_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for required imports
            required_imports = ['requests', 'json', 'uuid']
            for import_name in required_imports:
                if f"import {import_name}" not in content and f"from {import_name}" not in content:
                    self.warnings.append(f"Missing import: {import_name}")
            
            # Check for API key placeholder
            if "your-api-key-here" not in content:
                self.warnings.append("API key placeholder not found in examples")
            
            print("✅ Python examples are valid")
            return True
            
        except Exception as e:
            self.errors.append(f"Error validating examples: {e}")
            return False
    
    def run_validation(self) -> bool:
        """
        Run all validation checks.
        
        Returns:
            True if all validations pass, False otherwise
        """
        print("🚀 Starting LetsCloud GPT Actions Configuration Validation")
        print("=" * 60)
        
        validations = [
            self.validate_file_structure,
            self.validate_openapi_spec,
            self.validate_examples,
            self.validate_urls
        ]
        
        all_passed = True
        for validation in validations:
            try:
                if not validation():
                    all_passed = False
            except Exception as e:
                self.errors.append(f"Validation error: {e}")
                all_passed = False
        
        print("\n" + "=" * 60)
        print("📊 VALIDATION RESULTS")
        print("=" * 60)
        
        if self.errors:
            print(f"❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"   • {error}")
        
        if self.warnings:
            print(f"⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"   • {warning}")
        
        if not self.errors and not self.warnings:
            print("🎉 All validations passed! Configuration is ready for deployment.")
        elif not self.errors:
            print("✅ Configuration is valid with some warnings.")
        else:
            print("❌ Configuration has errors that need to be fixed.")
        
        return all_passed


def main():
    """Main function."""
    validator = ConfigValidator()
    
    try:
        success = validator.run_validation()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⏹️  Validation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
