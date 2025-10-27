
# example
    .env file: API_KEY = "***"  
    source gpt-env/bin/activate  
    python3 chat.py -q "give example of the code '            
                case OP_SUPER_INVOKE:
                ObjStr* method = READ_STR();
                int argCnt = READ_BYTE();
                ObjClass* superclass = AS_CLASS(pop());'"  

# requirements
    python3 -m venv gpt-env  
    pip3 install openai  
  