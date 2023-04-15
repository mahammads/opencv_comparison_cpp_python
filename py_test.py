import ctypes
import chardet
import datetime
import subprocess as sp
import io

def pdf2text_cpp(path):
    dll_name = "/home/jubers/cpp_test/libpdf2text.so"
    # dll_handle = win32api.LoadLibraryEx(dll_name, 0, win32con.LOAD_WITH_ALTERED_SEARCH_PATH)
    lib = ctypes.CDLL(dll_name)

    # Define the function prototype
    lib.pdf_extract.argtypes = [ctypes.c_char_p]
    lib.pdf_extract.restype = ctypes.c_char_p

    # Call the function
    result = lib.pdf_extract(path.encode('utf-8'))
    return result.decode('utf-8')



def pdf2text_poplr(pdf_name):
    """convert pdf to text using poppler by preserving the format.

    :param pdf_name: input pdf name
    :type pdf_name: string
    :return: extracted text
    :rtype: string
    """        
    ##---------------------------------------------------------------------------------------##
    ## This function extracts text from the pdf by preserving the format                     ##
    ##---------------------------------------------------------------------------------------##
    poppler_path_exe = "/usr/bin/pdftotext"
    try:
        text_file_name = pdf_name + ".txt"
        # output_file = os.path.join(output_text_files, text_file_name)
        args = [poppler_path_exe, "-layout", pdf_name, "-"]
        cp = sp.run(args, stdout=sp.PIPE, stderr=sp.DEVNULL, check=True, text=True, encoding="utf8")
        text = cp.stdout
        with open(text_file_name, 'w', encoding="utf8") as f:
            f.write(cp.stdout)
        return text
        # return cp.stdout
    except Exception as err:
        raise err
    
if __name__ == "__main__":
   
    path = "/home/jubers/cpp_test/sample-pdf-download-10-mb.pdf"
   
    st_time = datetime.datetime.now()
    result = pdf2text_cpp(path)
    # print(result)
    end_time = datetime.datetime.now()
    print(f"total time taken to extract on cpp: {end_time-st_time}")
    
    st_time = datetime.datetime.now()
    result = pdf2text_poplr(path)
    # print(result)
    end_time = datetime.datetime.now()
    print(f"total time taken to extract on python: {end_time-st_time}")