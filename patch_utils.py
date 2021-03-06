import argparse
import sys
import logging
import os
from utils import get_arg_parser, manage_linux_repo
from create_patches import get_commit_list, create_patch_files
from test_patches import test_patches
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

# TODO(BOGDAN): Add verbose logging

def create_patches(args):
    if not args.linux_repo:
        args.linux_repo = '/root/linux'
        manage_linux_repo(args.linux_repo, create=True)
    else:
        manage_linux_repo(args.linux_repo)

    os.chdir(args.linux_repo)
    commit_list = get_commit_list(args.linux_repo, args.date, args.author)
    
    patch_list = create_patch_files(commit_list, args.patches_folder)
    logger.info('Created the following patches:')
    [logger.info(patch_path) for patch_path in patch_list]

if __name__ == '__main__':
    parser = get_arg_parser()
    args = parser.parse_args(sys.argv[1:])

    command = sys.argv[1]
    if command == 'create-patches':
        create_patches(args)
    elif command == 'test-patches':
        test_patches(args.patches_folder)
    else:
        pass