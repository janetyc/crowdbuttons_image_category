####How to distribute HITs on Mturk?
- modify "aws-mturk-clt-1.3.1/bin/mturk.propertie"
  * access_key=[YOUR ACCESS KEY]
  * secret_key=[YOUR SECRET KEY]
  * use sandbox

    ```
    service_url=https://mechanicalturk.sandbox.amazonaws.com/?Service=AWSMechanicalTurkRequester
    ```

    OR mturk

    ```
    service_url=https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
    ```
- sh run.sh (distribute HITs and generate xxx.success or xxx.failure)
- sh getResults.sh (generate xxx.results)
- sh generateResultsSummary.sh (generate xxx.summary)

####How to get report from xxx.results or xxx.summary?
- python check_result.py xxx.results (only generate result.txt)
  python check_result.py xxx.reaults true (generate result.txt and mturk_labels.txt)
- python check_summary.py xxx.summary (generate summary.txt)
