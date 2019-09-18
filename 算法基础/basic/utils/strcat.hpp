char* _strcat(char* dst, const char* src)
{
    if(dst==nullptr || src==nullptr){
        return nullptr;
    }
    char* ret = dst;
    while(*dst != '\0') ++dst;
    while( (*dst++ = *src++) != '\0' );
    return ret;
}