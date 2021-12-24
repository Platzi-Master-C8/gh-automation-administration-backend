# GetHired Automation Administration Backend ![version](https://img.shields.io/github/v/tag/Platzi-Master-C8/gethired-automation-administration-backend?label=version&logo=github)

This project is intended to be an accounts and permissions manager for the
GetHired platform.

## Build

### Prerequisites

- Copy `.env.example` to `.env` and fill with desired values.

- In order to work properly NPM, Docker Engine and Docker Compose must be
  installed in advance on operative system.

#### Windows

Docker counts with an UI for managing containers. A complete guide about
installation can be found in the [official Docker documentation](https://docs.docker.com/desktop/windows/install/).

#### MacOS

Same case as Windows, an UI can be installed, but according to the [official
Docker documentation](https://docs.docker.com/desktop/mac/install/) two variants
can be selected depending on the processor architecture.

#### Linux

For these distributions the Docker Engine needs some of tricky steps to be
installed. Depending on the distribution the commands changes. A complete list
of available distributions is shown on the [official Docker doucmentation](https://docs.docker.com/engine/install/).

### Development

> This configuration is intended to real time binding of local with container
> files.

Build image:

```bash
docker-compose build
```

Start sever with hot-reload, by defaul on `http://localhost:8000`. For debugging
purposes:

```bash
docker-compose up
```

If running in background is desired:

```bash
docker-compose up -d
```

Kill service

```bash
docker-compose down
```

### Production

#### Vercel

Install [Vercel CLI](https://vercel.com/cli) (on Windows and macOS administrator
privileges are required, on linux preced the command with `sudo`):

```bash
npm i -g vercel
```

Login to Vercel:
> Depending on login method, the command will ask for credentials or will show
> an URL to access through the browser.

```bash
vercel login
```

To deploy the project:

```bash
vercel .
```
