import argparse
import aws.queryS3
import classifyDirectory

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode", help="Detection mode")
    parser.add_argument("-p", "--path", help="Path")

    args = parser.parse_args()

    if args.mode == "aws":
        aws.queryS3.detect_from_aws()
    elif args.mode == "local":
        if args.path == None:
            print("Please specify a path with the '-p' flag")
        else:
            classifyDirectory.classify_directory(args.path, "/train_data.csv")
    else:
        print("Invalid mode... Please select a valid mode with the '-m' flag. Valid modes are: 'aws', 'local'")