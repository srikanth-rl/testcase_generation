import streamlit as st
import time


def generate_prompt_from_file(file):
    """Read and decode uploaded file as a string."""
    try:
        content = file.read().decode("utf-8")
        return content.strip()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return ""


def run_mock_ollama(prompt: str):
    """Mock function to simulate Ollama response, replace with actual API call if available."""
    try:
        start_time = time.time()

        # Simulated delay for processing
        time.sleep(2)

        # Simulated output for generated test cases
        output = f"Simulated test cases for prompt: '{prompt}'"

        end_time = time.time()
        elapsed_time = end_time - start_time

        return f"Execution Time: {elapsed_time:.2f} seconds\n\nGenerated Test Cases:\n{output}"
    except Exception as e:
        return f"Request failed: {e}"


def main():
    st.title("Prompt Upload and Processing")

    uploaded_file = st.file_uploader(
        "Choose a file containing the prompt", type="txt")
    if uploaded_file is not None:
        prompt = generate_prompt_from_file(uploaded_file)
        if prompt:
            editable_prompt = st.text_area(
                "Prompt Content (editable)", prompt, height=200)

            if st.button("Run Ollama (Simulated)"):
                result = run_mock_ollama(editable_prompt)

                # Display the output in a text area
                st.text_area("Output", result, height=300)

                # Show download button without closing the output
                st.download_button(
                    label="Download Output as TXT",
                    data=result,
                    file_name="ollama_output.txt",
                    mime="text/plain"
                )


if __name__ == "__main__":
    main()
