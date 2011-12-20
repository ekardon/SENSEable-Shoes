# This file is generated by Z:\Users\rgommers\Code\numpy\setup.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

atlas_threads_info={}
blas_opt_info={'libraries': ['f77blas', 'cblas', 'atlas'], 'library_dirs': ['C:\\local\\lib\\yop\\sse3'], 'language': 'c', 'define_macros': [('NO_ATLAS_INFO', -1)]}
atlas_blas_threads_info={}
lapack_opt_info={'libraries': ['lapack', 'f77blas', 'cblas', 'atlas'], 'library_dirs': ['C:\\local\\lib\\yop\\sse3'], 'language': 'f77', 'define_macros': [('NO_ATLAS_INFO', -1)]}
atlas_info={'libraries': ['lapack', 'f77blas', 'cblas', 'atlas'], 'library_dirs': ['C:\\local\\lib\\yop\\sse3'], 'language': 'f77', 'define_macros': [('NO_ATLAS_INFO', -1)]}
lapack_mkl_info={}
blas_mkl_info={}
atlas_blas_info={'libraries': ['f77blas', 'cblas', 'atlas'], 'library_dirs': ['C:\\local\\lib\\yop\\sse3'], 'language': 'c', 'define_macros': [('NO_ATLAS_INFO', -1)]}
mkl_info={}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    