{
    "targets": [
        {
            "target_name": "starspace",
            "sources": [
                "vendor/StarSpace/src/data.cpp",
                "vendor/StarSpace/src/data.h",
                "vendor/StarSpace/src/dict.cpp",
                "vendor/StarSpace/src/dict.h",
                "vendor/StarSpace/src/doc_data.cpp",
                "vendor/StarSpace/src/doc_data.h",
                "vendor/StarSpace/src/doc_parser.cpp",
                "vendor/StarSpace/src/doc_parser.h",
                "vendor/StarSpace/src/matrix.h",
                "vendor/StarSpace/src/model.cpp",
                "vendor/StarSpace/src/model.h",
                "vendor/StarSpace/src/parser.cpp",
                "vendor/StarSpace/src/parser.h",
                "vendor/StarSpace/src/proj.cpp",
                "vendor/StarSpace/src/proj.h",
                "vendor/StarSpace/src/starspace.cpp",
                "vendor/StarSpace/src/starspace.h"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "/usr/local/bin/boost_1_63_0/"
            ],
            "cflags": [
                "-std=c++11",
                "-pthread",
                "-Wsign-compare",
                "-fexceptions",
                "-O0"
            ],
            "conditions": [
                [ 'OS!="win"', {
                    "cflags+": [ "-std=c++11", "-fexceptions" ],
                    "cflags_c+": [ "-std=c++11", "-fexceptions" ],
                    "cflags_cc+": [ "-std=c++11", "-fexceptions" ],
                }],
                [ 'OS=="mac"', {
                    "cflags+": [ "-stdlib=libc++" ],
                    "xcode_settings": {
                        # need typeid so -frtti
                        "OTHER_CPLUSPLUSFLAGS" : [ "-std=c++11", "-stdlib=libc++", "-pthread", "-frtti" ],
                        "OTHER_LDFLAGS": [ "-stdlib=libc++" ],
                        "MACOSX_DEPLOYMENT_TARGET": "10.7",
                        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                        "CLANG_CXX_LANGUAGE_STANDARD":"c++11",
                        "CLANG_CXX_LIBRARY": "libc++"
                    },
                }]
            ]
        },
        {
            "target_name": "action_after_build",
            "type": "none",
            "dependencies": [ "<(module_name)" ],
            "copies": [
                {
                    "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
                    "destination": "<(module_path)"
                }
            ]
        }
    ]
}