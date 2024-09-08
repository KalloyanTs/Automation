import sys
import json
import io

def read_documents_from_stdin():
    # Read the entire input from stdin
    input_data = sys.stdin.read()
    
    # Parse the JSON data
    documents = json.loads(input_data)
    
    # Convert keys to integers (if they are not already)
    documents = {int(k): v for k, v in documents.items()}

    execute(documents)
    
def execute(documents):
    inverted_index = {}
    
    # Implement the inverted index creation
    for doc_id, words in documents.items():
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = []
            inverted_index[word].append(doc_id)
    
    print(inverted_index)

# Example usage
if __name__ == "__main__":
    # Example input for testing
    example_input = json.dumps({
        1: ['apple', 'banana', 'cabbage'],
        2: ['banana', 'carrot', 'apple'],
        3: ['apple', 'carrot', 'banana', 'lettuce']
    })
    
    # Simulate reading from stdin
    sys.stdin = io.StringIO(example_input)
    
    read_documents_from_stdin()
