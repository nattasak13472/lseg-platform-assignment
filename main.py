import argparse
import json
import sys

def get_nested_value(obj_data, key_path) :
    
    list_obj_result = []
    
    keys = key_path.split('/')
    key_depth = len(keys)
    
    if isinstance(obj_data, dict) :
        
        # ITERATE OVER KEYS
        for index, key in enumerate(keys) :
            
            # 1ST ROUND : DEFAULT CURRENT LEVEL OBJECT => FIRST LEVEL
            current_obj_level = obj_data
            if index > 0 :
                # N ROUND : SET CURRENT LEVEL OBJECT => RESULT PREVIOUS LEVEL
                current_obj_level = list_obj_result[index-1]
            
            # GET OBJECT BY KEY
            if key in current_obj_level:
                list_obj_result.append(current_obj_level[key])
            else:
                raise KeyError(f"Invalid entered key `{key}`, in nested object level {index+1} : {json.dumps(current_obj_level)}")
            
    else:
        raise TypeError(f"Object is invalid")
        
    return list_obj_result[key_depth-1]

def main():
    
    parser = argparse.ArgumentParser(description="Get value from nested json object.")
    parser.add_argument(
        '-obj', 
        '--object',
        required=True,
        help='JSON Object, for example: \'{“a”:{“b”:{“c”:”d”}}}\''
    )
    parser.add_argument(
        '-k', 
        '--key',
        required=True,
        help='key to get value from nested json object, for example: \'a/b/c\''
    )
    args = parser.parse_args()
    
    # READ JSON
    try:
        obj = json.loads(args.object)
    except json.JSONDecodeError as err:
        print("Invalid json object from argument --object")
        sys.exit(1)
        
    # START GET NESTED VALUE
    try:
        
        value = get_nested_value(obj, args.key)
        
        print(f"RESULT VALUE : {value}")
        
    except KeyError as err:
        print(f"KEY ERROR: {err}", file=sys.stderr)
        sys.exit(1)
    except TypeError as err:
        print(f"TYPE ERROR : {err}", file=sys.stderr)
        sys.exit(1)
    

if __name__ == '__main__':
    main()