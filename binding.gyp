{
    "targets": [
        {
            "target_name": "starspace",
            "sources": [
                "vendor/StarSpace/src/utils/normalize.cpp",
                "vendor/StarSpace/src/utils/args.cpp",
                "vendor/StarSpace/src/dict.cpp",
                "vendor/StarSpace/src/proj.cpp",
                "vendor/StarSpace/src/parser.cpp",
                "vendor/StarSpace/src/model.cpp",
                "vendor/StarSpace/src/starspace.cpp",
                "vendor/StarSpace/src/doc_parser.cpp",
                "vendor/StarSpace/src/utils/utils.cpp",
                "vendor/StarSpace/src/main.cpp"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "/usr/local/bin/boost_1_63_0/"
            ],
            "cflags": [
                "-std=gnu++11",
                "-pthread",
                # "-Wsign-compare",
                "-fexceptions",
                "-O3",
                "-funroll-loops"
            ],
            "conditions": [
                [ 'OS!="win"', {
                    "cflags+": [ "-std=gnu++11", "-fexceptions" ],
                    "cflags_c+": [ "-std=gnu++11", "-fexceptions" ],
                    "cflags_cc+": [ "-std=gnu++11", "-fexceptions" ],
                }],
                [ 'OS=="mac"', {
                    "cflags+": [ "-stdlib=libc++" ],
                    "xcode_settings": {
                        # need typeid so -frtti ; also, dont want to see sign compare warning
                        "OTHER_CPLUSPLUSFLAGS" : [ "-std=gnu++11", "-stdlib=libc++", "-pthread", "-frtti", "-Wno-sign-compare" ],
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