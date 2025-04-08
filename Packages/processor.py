import DataProcessing.reader as reader
import DataProcessing.writer as writer

contents = reader.read_data("input.txt")
print(contents)

print(writer.write_data("output.txt"))  # Output: Writing data to output.txt
