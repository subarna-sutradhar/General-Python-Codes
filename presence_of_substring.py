def search_string():
    import re
    substring='water'
    search1=re.search(substring,'Water water everywhere but not a drop to drink')
    if search1:
        position=search1.start()
        print("matched", substring, "at position", position)
    else:
        print("No match found")

"""Another way is using meta search"""
def metasearch():
    import re
    p=re.compile('sing+')
    search1=re.search(p,'Some singers sing well')
    if search1:
        match=search1.group()
        index=search1.start()
        lindex=search1.end()
        print("matched", match, "at index", index ,"ending at" ,lindex)
    else:
        print("No match found")
 