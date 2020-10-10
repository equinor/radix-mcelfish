# Radix Playground: McElfish

To run the project locally, you need docker:

```
docker build -t mcelfish .
docker run -p 8000:8000 mcelfish
```


# Steps for setting up a Radix service


## Setting up the repository

1. Create a repository on GitHub (e.g.) `equinor/radix-mcelfish` (public)
1. add collaborators to have triage/write/maintain access
1. Warning: GitHub now defaults to `main` as the initial branch, but
   Radix expects `master`.  You might need to change the default branch.


## Follow the _Getting Started_ guide

1. Create configuration file (`radixconfig.yaml`)
1. Register Radix playground app in the [console](https://console.playground.radix.equinor.com/applications)
1. Add deploy key according to the guide
1. Add webhook according to the guide

## Kickstart the pipelines

For each environment (`prod`, `dev`, `test`, `qa`, etc) you might need
to manually start the new job.

Press _new job_ under `/applications/<name>/jobs/new`.


# Resources and inspiration

- [radix.equinor.com](https://www.radix.equinor.com)
- [radix.equinor.com/guides/getting-started/](https://www.radix.equinor.com/guides/getting-started/)
- [github.com/keaaa/hello-world](https://github.com/keaaa/hello-world)
- [github.com/equinor/radix-example-workshop-1](https://github.com/equinor/radix-example-workshop-1)
- [console.playground.radix.equinor.com/applications/xample-5-nodejs/envs/prod/component/x5n](https://console.playground.radix.equinor.com/applications/xample-5-nodejs/envs/prod/component/x5n)
