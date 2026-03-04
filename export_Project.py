import os

def export_only_code(output_file="project_code_only.txt"):
    # শুধুমাত্র এই এক্সটেনশনগুলো আমরা নেব
    allowed_extensions = {'.py', '.yaml', '.yml', '.json','.ipynb', '.html','pipeline','research','src'}
    
    # এই ফোল্ডারগুলো পুরোপুরি বাদ দেব
    exclude_dirs = {
        '.git', '__pycache__', '.pytest_cache', 'venv','pricing', 'env', 
        'pricing_engine.egg-info', 'artifacts', 'data', 'notebooks'
    }

    with open(output_file, "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if any(file.endswith(ext) for ext in allowed_extensions):
                    if file == output_file or file == "export_project.py":
                        continue
                        
                    file_path = os.path.join(root, file)
                    f.write(f"\n{'='*50}\n")
                    f.write(f"FILE: {file_path}\n")
                    f.write(f"{'='*50}\n\n")
                    try:
                        with open(file_path, "r", encoding="utf-8") as source_file:
                            f.write(source_file.read())
                    except Exception:
                        f.write(f"Skipped: Could not read {file_path}\n")
                    f.write("\n")

if __name__ == "__main__":
    export_only_code()
    print("Done! 'project_code_only.txt' তৈরি হয়েছে। এখন এটি আপলোড করুন।")