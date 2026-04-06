import os
import sys
import subprocess
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from services.config_service import ConfigService

class PerformanceService:
    def __init__(self):
        self.config_service = ConfigService()
        self.payload_dir = self.config_service.payload_dir
        self.levels = ['low', 'medium', 'high', 'extreme']

    def run_test(self, data):
        config = self.config_service.get_config()
        datafile = data.get('datafile', 'data')
        
        results = {}
        for level in self.levels:
            cmd = ['python', 'payload.py', config['aim'], config['cipher'], datafile, level]
            success, output = self.config_service.run_command(cmd, self.payload_dir)
            
            if not success:
                return {'success': False, 'message': f'Test failed for {level}: {output}'}
            
            try:
                cycles = int(output.strip().split('\n')[-1])
                results[level] = cycles
            except (ValueError, IndexError):
                results[level] = 0
        
        return {'success': True, 'results': results}

    def compare_results(self, files):
        comparison_data = {}
        
        for filepath in files:
            try:
                with open(filepath, 'r') as f:
                    data = f.readlines()[0].strip().split(' ')
                    values = list(map(int, data))
                    filename = os.path.basename(filepath).split('.')[0]
                    comparison_data[filename] = values
            except Exception as e:
                return {'success': False, 'message': f'Failed to read {filepath}: {str(e)}'}
        
        return {'success': True, 'comparison_data': comparison_data}

    def save_result(self, data):
        results = data.get('results', {})
        filepath = data.get('filepath', 'performance_result.txt')
        
        try:
            with open(filepath, 'w') as f:
                f.write(' '.join(map(str, [results.get(level, 0) for level in self.levels])))
            return {'success': True, 'filepath': filepath}
        except Exception as e:
            return {'success': False, 'message': f'Failed to save: {str(e)}'}
