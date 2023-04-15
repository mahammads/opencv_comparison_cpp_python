#include <poppler/cpp/poppler-document.h>
#include <poppler/cpp/poppler-page.h>
#include <iostream>
#include <string>
using namespace std;

extern "C" {
const char* pdf_extract(const char* path) {
    static string output;
    string file_name = string(path);
    auto document = poppler::document::load_from_file(file_name);
    if (!document) {
        cerr << "Error: could not load PDF document" << endl;
        return "error";
    }

    for (int i = 0; i < document->pages(); ++i) {
        auto page = document->create_page(i);
        if (!page) {
            cerr << "Error: could not load page " << i << endl;
            continue;
        }

        output += page->text().to_utf8().data();
    }
    return output.c_str();
    }
}

int main(){
    const char* path = "/home/jubers/cpp_test/Mahamad_resume.pdf";
    string result = pdf_extract(path);
    cout << result << endl;
}