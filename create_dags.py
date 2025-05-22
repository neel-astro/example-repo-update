import os

# Path to the example DAG file
example_dag_path = "astro-project/dags/example_dag_basic.py"
# Directory where new DAGs will be created
output_dir = "astro-project/dags"

# Read the content of the example DAG file
with open(example_dag_path, "r") as f:
    example_content = f.read()

# Create 700 DAG files
for i in range(1, 701):
    # Replace the DAG ID
    new_content = example_content.replace("example_dag_basic", f"example_dag_basic_{i}")
    
    # Create new file with updated content
    new_file_path = os.path.join(output_dir, f"example_{i}.py")
    with open(new_file_path, "w") as f:
        f.write(new_content)
    
    print(f"Created {new_file_path}")

print("Successfully created 700 DAG files!")
