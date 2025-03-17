import streamlit as st
import json

#load and save library
def load_library():
    try:
        with open("library.json" ,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_library():
    with open("library.json" , "w") as file:
        json.dump(library,file,indent=4)

library=load_library()

st.title("Personal Library Manager")
menu=st.sidebar.radio("Select an option" , ["View Library","Add Book","Remove Book","Search Book","Save and Exit"])
if menu == "View Library":
    st.sidebar.title("Your Library")
    
    if library:  
        st.table(library)
    else:
        st.write("Your library is empty. Add some books!")
elif menu == "Add Book":
    st.sidebar.title("Add a new book")
    
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=1990, max_value=2030, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark as read")

    if st.button("Add Book"): 
        library.append({
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read_status": read_status
        })
        save_library()  
        st.success("Book Added Successfully")
        st.rerun()
elif menu == "Remove Book":
    st.sidebar.title("Remove a Book")
    book_titles=[book["title"] for book in library]
    if book_titles:
        selected_book=st.selectbox("Select a book to remove",book_titles)
        if st.button("Remove Book"):
            library=[book for book in library if book["title"] != selected_book]
            save_library()
            st.success("Book Removed successfully")
            st.rerun()
    else:
            st.warning("no books in your library !")
elif menu == "Remove a Book ❌":
    st.header("🗑️ Remove a Book")
    book_titles = [book["title"] for book in library]
    if book_titles:
        selected_book = st.selectbox("📖 Select a book to remove", book_titles, key="remove_book")
        
        if st.button("❌ Remove Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("🚀 Book Removed Successfully! 📖")
            st.rerun()
    else:
        st.warning("📭 No books available to remove!")

elif menu == "Save and Exit":
    save_library()
    st.success("Library saved successfully")