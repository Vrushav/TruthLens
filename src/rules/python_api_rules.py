PYTHON_API_RULES = {

    "requests": {
        "valid": {
            "get",
            "post",
            "put",
            "delete",
            "patch",
            "head",
            "options"
        }
    },

    "pandas": {
        "valid": {
            "read_csv",
            "read_excel",
            "DataFrame",
            "concat",
            "merge"
        }
    },

    "numpy": {
        "valid": {
            "array",
            "zeros",
            "ones",
            "mean",
            "sum",
            "linspace"
        }
    }

}