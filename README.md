# register-deployment-with-linearb

A GitHub Action that registers deployments with LinearB using LinearB Deployment API.

## Prerequisites

- A LinearB API token is required. You can obtain this from your [LinearB account settings](https://linearb.helpdocs.io/article/79fmogrxw3-how-to-generate-release-api-tokens).
- The repository must be connected to LinearB.

## Usage

Add this action to your workflow:

```yaml
- name: Register Deployment with LinearB
  uses: danielinclouds/register-deployment-with-linearb@v1
  with:
    api_token: ${{ secrets.LINEARB_API_TOKEN }}
    repo_url: 'https://github.com/${{ github.repository }}.git'
    ref_name: ${{ github.sha }}
```

## Inputs
| Input       | Required | Default | Description                                                                |
|-------------|----------|---------|----------------------------------------------------------------------------|
| `api_token` | Yes      |         | API token for authenticating with the LinearB API                          | 
| `repo_url`  | Yes      |         | The URL of the repository (e.g. https://github.com/org/repo.git)           |
| `ref_name`  | Yes      |         | Ref name of the release, accepts any Git ref (i.e. commit short or long sha/tag name) |
| `timestamp` | No       |         | Timestamp in ISO 8601 format (e.g. 2022-03-14T22:23:34Z)                   |
| `stage`     | No       |         | The key of the custom pre-deployment stage                                 |
| `services`  | No       |         | The list of LinearB services names (e.g. service1,service2).               |

## Outputs 
This action doesn't produce any outputs, but it will print the API response status and content to the workflow logs.  

## Links

[LinearB API Docs](https://docs.linearb.io/api-deployments/)
