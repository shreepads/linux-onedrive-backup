# linux-onedrive-backup

Backup files on MS OneDrive from Linux. 

Note that the step to upload the encrypted backup files into MS OneDrive is handled from
a browser e.g. Firefox.

This repo provides 
* Steps on how to backup files to OneDrive
* A tool that can be used to compare hashes to check the encrypted files were stored properly.
  See the webapp/ README for details about this tool.
* Steps to restore the backup from OneDrive

## Why

The natural question is why one would be crazy enough to adopt this Rube Goldberg-esque
manual backup process. A few reasons that apply to me, at the moment, in the form of a Q&A.
* Why not a home NAS: I don't have the time and resources (including stable power supply)
  to setup a home NAS solution that can provide comparable redundancy at a comparable cost.
  Also it would not be portable.
* Why not use AWS S3 or something similar: Cost; under my family plan I get OneDrive storage
  at less than $1 per month per TB, nothing else comes close. Of course OneDrive doesn't
  provide resiliency and availability SLAs for personal accounts similar to S3 or other
  cloud object storage. The less said about Google cloud storage the better!
* Why not a proper encrypted automated backup solution like Tarsnap or Spideroak: First,
  I think Microsoft will be more viable, long term, than minor players like Tarsnap and
  Spideroak. Spideroak is a lot more expensive than OneDrive and its desktop client is closed
  source. Tarsnap is great, but again more expensive than OneDrive even after taking dedup
  savings into account.
* Why use the OneDrive web UI to upload files manually: Microsoft doesn't provide a Linux
  client, there are third party clients but I don't trust they will be maintained or function
  correctly.
* Why the special local app just to verify the hashes of the uploaded data: The OneDrive web
  UI doesn't provide this information at all, let alone in a way that allows for an easy compare.

## Backup

1. Create a zip archive of a given folder e.g. `important-2020-03-30.zip` and verify it. I
   use zip as it has integrity checking and good cross-platform support but you can use any
   archival format convenient.

1. Encrypt the zip file using gpg and a long and complex passphrase (defaults to AES encryption
   as of GnuPG 2.2)

   `$ gpg -cv important-2020-03-30.zip`
	
1. Split the resulting file `important-2020-03-30.zip.gpg` into chunks that can be easily uploaded
   from your browser using OneDrive's web interface and the reliability and speed of your
   network connection (e.g. 100MB, 1GB). Note that I've found the OneDrive Web UI more
   reliable and faster for uploading than downloading and so recommend not using chunks
   bigger than 1GB unless you have a very fast and stable internet connection.

   `$ split -b 100M important-2020-03-30.zip.gpg important-2020-03-30.zip.gpg.`
   
   `$ split -b 1G important-2020-03-30.zip.gpg important-2020-03-30.zip.gpg.`

1. Calculate MD5, SHA1 and SHA256 sums of the full GPG files and the split GPG files and
   write these to 3 separate files. While OneDrive currently only computes SHA1 sums,
   this may change in the future (although its unlikely MD5 would be used, I've generated
   it as it's used by AWS S3).
   
   `$ sha1sum * > important-2020-03-30-sha1sums.txt`

   `$ md5sum * > important-2020-03-30-md5sums.txt`
   
   `$ sha256sum * > important-2020-03-30-sha256sums.txt`

1. Sign-in to OneDrive's web UI, create an appropriate folder structure and upload the
   split GPG files and the 3 files containing the MD5, SHA1 and SHA256 hashsums.
   The web UI is able to handle multiple uploads and queuing of requests.

1. Once the upload is complete, start the webapp and compare the split GPG SHA1 sums
   reported by the tool (using the OneDrive API) with the values computed in Step 4. See
   the /webapp README for details. 

1. Usually the files are uploaded correctly and the SHA1 hashes match but I have come
   across an error once. In that case simply re-upload the specific file(s) where there
   is a mismatch and re-validate the SHA1 sums.

1. Delete the split GPG files and the single GPG file. If you're paranoid (like me!) do a
   test restore using either the local split gpg files or the ones downloaded from OneDrive
   before deleting these GPG files. Maintain the ZIP file created in Step 1 as long as
   practical (e.g. the next backup cycle).


## Restore

1. Sign-in to OneDrive's web UI and download the split GPG files and the hashsum files.
   As mentioned above the download interface is less reliable and slower than upload.

1. Join the split gpg files into the single one

   `$ cat important-2020-03-30.zip.gpg.?? > important-2020-03-30.zip.gpg`
   
1. Verify the hash of the reassembled full GPG file with the original. If any discrepancies
   are found compare the hashes of the split GPGs, one or more download may have been corrupted.

1. Decrypt the gpg file using the long passphrase

   `$ gpg important-2020-03-30.zip.gpg`
   
1. Unzip the folder

