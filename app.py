import streamlit as st
from core.comment_generator import generate_comments
from core.inserter import insert_comments
from core.analyzer import analyze_code_structure
from core.utils import save_code

# Page setup
st.set_page_config(page_title="Java Comment Generator", page_icon="💬", layout="wide")

st.title("💬 J-CommentGen")
st.markdown("Automatically add AI-generated comments to your Java code")
st.markdown("---")

# Initialize session state
if 'code' not in st.session_state:
    st.session_state.code = ""
if 'filename' not in st.session_state:
    st.session_state.filename = "code.java"
if 'uploaded_file_content' not in st.session_state:
    st.session_state.uploaded_file_content = None
if 'pasted_code' not in st.session_state:
    st.session_state.pasted_code = ""
if 'upload_results' not in st.session_state:
    st.session_state.upload_results = None
if 'paste_results' not in st.session_state:
    st.session_state.paste_results = None
if 'upload_analysis' not in st.session_state:
    st.session_state.upload_analysis = None
if 'paste_analysis' not in st.session_state:
    st.session_state.paste_analysis = None

# Step 1: Input
st.markdown("### 📁 Input Your Java Code")

input_method = st.radio("Choose input method:", ["Upload File", "Paste Code"], horizontal=True)

if input_method == "Upload File":
    col1, col2 = st.columns([4, 1])
    
    with col1:
        uploaded_file = st.file_uploader("Choose a Java file", type=["java"])
    
    with col2:
        st.write("")
        st.write("")
        st.write("")
        if st.button("🗑️ Clear File"):
            st.session_state.uploaded_file_content = None
            st.session_state.filename = "code.java"
            st.session_state.upload_results = None
            st.session_state.upload_analysis = None
            st.rerun()
    
    if uploaded_file:
        file_content = uploaded_file.read().decode("utf-8")
        st.session_state.uploaded_file_content = file_content
        st.session_state.filename = uploaded_file.name
    
    if st.session_state.uploaded_file_content:
        code = st.session_state.uploaded_file_content
        filename = st.session_state.filename
        st.success(f"✓ Loaded: {filename}")
        
        if st.button("👁️ Preview File"):
            st.code(code, language="java", line_numbers=True)
    else:
        code = ""
        filename = "code.java"
    
    current_results = st.session_state.upload_results
    current_analysis = st.session_state.upload_analysis
        
else:
    col1, col2 = st.columns([4, 1])
    
    with col1:
        pasted_code = st.text_area(
            "Paste your Java code:", 
            height=250, 
            placeholder="public class Example {\n    // Your code here\n}",
            value=st.session_state.pasted_code,
            key="paste_area"
        )
    
    with col2:
        st.write("")
        st.write("")
        st.write("")
        if st.button("🗑️ Clear Code"):
            st.session_state.pasted_code = ""
            st.session_state.paste_results = None
            st.session_state.paste_analysis = None
            st.rerun()
    
    st.session_state.pasted_code = pasted_code
    code = st.session_state.pasted_code
    filename = "code.java"
    
    current_results = st.session_state.paste_results
    current_analysis = st.session_state.paste_analysis

st.markdown("---")

# Step 2: Generate
st.markdown("### ⚡Generate Comments")

if st.button("✨ Generate Comments", type="primary", use_container_width=True):
    if not code.strip():
        st.error("❌ No code provided! Please upload a file or paste code first.")
    else:
        with st.spinner("🔄 Processing..."):
            try:
                analysis = analyze_code_structure(code)
                commented = generate_comments(code)
                merged = insert_comments(code, commented)
                
                if input_method == "Upload File":
                    st.session_state.upload_results = merged
                    st.session_state.upload_analysis = analysis
                else:
                    st.session_state.paste_results = merged
                    st.session_state.paste_analysis = analysis
                
                current_results = merged
                current_analysis = analysis
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                current_results = None
                current_analysis = None

# Step 3: Results
if current_results:
    st.markdown("---")
    st.markdown("### 📊 Results")
    
    tab1, tab2 = st.tabs(["📝 Commented Code", "📊 Analysis"])
    
    with tab1:
        st.code(current_results, language="java", line_numbers=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.download_button(
                "⬇️ Download File",
                current_results,
                file_name=f"commented_{filename}",
                mime="text/x-java",
                type="primary",
                use_container_width=True
            )
        
        with col2:
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                st.text_area(
                    "Select all and copy:",
                    value=current_results,
                    height=300,
                    key="copy_output"
                )
                st.caption("💡 Press Ctrl+A then Ctrl+C to copy.")
        
        with col3:
            if st.button("💾 Save to Local File", use_container_width=True):
                save_path = f"saved_{filename}"
                save_code(save_path, current_results)
                st.success(f"Saved locally as: {save_path}")

    with tab2:
        if current_analysis:
            st.json(current_analysis)

st.markdown("---")
st.caption("🤖 Powered by AI | Easy code documentation")
