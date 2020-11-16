# linux-onedrive-backup

Backup files on MS OneDrive from Linux. 

Note that the step to upload the encrypted backup files into MS OneDrive is handled from a browser e.g. Firefox.

This repo provides 
* Steps on how to backup files to OneDrive
* A tool that can be used to compare hashes to check the encrypted files were stored properly
* Steps to restore the backup


## Backup

1. Create a zip archive of a given folder e.g. `important.zip`

1. Encrypt the zip file using gpg and a long and complex passphrase:

   `$ gpg -c important.zip`
	
1. Split the resulting file `important.zip.gpg` into chunks that can be easily uploaded from your browser using Onedrive's web interface and the reliability and speed of your network connection (e.g. 100MB, 1GB)

   `$ split -b 100M important.zip.gpg important.zip.gpg.`
   
   `$ split -b 1G important.zip.gpg important.zip.gpg.`

1. Calculate MD5, SHA1 and SHA256 sums of the full GPG files and the split GPG files and write these to 3 separate files

1. Sign-in to Onedrive's web UI, create an appropriate folder structure and upload the split GPG files and the hashsum files. The web UI is able to handle multiple uploads and queuing of requests.

1. Once the upload is complete, start the webapp and compare the split GPG hashsums reported by the tool (using the OneDrive API) with the computed values. See the /webapp README for details.

1. Delete the split GPG files and the single GPG file. Maintain the ZIP file created in Step 1 as long as practical.


## Restore

1. Sign-in to Onedrive's web UI and download the split GPG files and the hashsum files.

1. Join the split gpg files into the single one

   `$ cat important.zip.gpg.?? > important.zip.gpg`
   
1. Verify the hash of the reassembled full GPG file with the original. If any discrepancies are found compare the hashes of the split GPGs, one or more download may have been corrupted.

1. Decrypt the gpg file using the long passphrase

   `$ gpg important.zip.gpg`
   
1. Unzip the folder

