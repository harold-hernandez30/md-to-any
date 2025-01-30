

class SupportedFiles:

    supported_extensions = (
        "md",
    )

    excluded_directories = (
        # Hidden directories
        ".", 
        "Brainstorm",
    )


    @staticmethod
    def is_content_file_supported(filename):
        return filename.endswith(tuple(SupportedFiles.supported_extensions))


    @staticmethod
    def is_directory_excluded(filename):
        return filename.endswith(tuple(SupportedFiles.excluded_directories))
    