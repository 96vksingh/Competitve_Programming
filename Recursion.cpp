bool checksequenece(char large[] , char*small) {
if(large[0]=='\0'){
    return false;
}
    int i=0;
    while(large[i]!='\0'){
        if(*small==large[i])
            return true;
        i++;
    }
        return *small==large[0]?checksequenece(large+1,small):false;
}
