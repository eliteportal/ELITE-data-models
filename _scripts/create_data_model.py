import pandas as pd
import yaml

with open(r"../config.yaml", 'r') as f:
    config = yaml.safe_load(f)

# paths to import files
root_path = config['paths']['root']
schematic_config = config['paths']['schematic']
csv_model = config['names']['csv_model']
json_model = config['names']['json_model']
# manifest_path = "C:/Users/nlee/Documents/Projects/schematic/schematic/tests/data/mock_manifests/example_biospecimen_test.csv"

# connect to synapse
os.system(f"run C:/Users/nlee/Documents/Projects/utils/syanpse_login.py")

# get data model
# test_model = pd.read_csv(syn.get("syn51401647").path)

# Initialize schematic

os.system(f"schematic init --config {config['paths']['schematic']}")

# Convert Schema
os.system(f"schematic schema convert {config['names']['csv_model']} --output_json {config['names']['json_model']}")

# Get an empty manifest as a CSV using model
os.system(f"schematic manifest --config config['paths']['schematic'] get")

# Validate Manifest
os.system(f"schematic model --config config['paths']['schematic'] /
    validate --manifest_path  manifest_path/
    --data_type Biospecimen")
