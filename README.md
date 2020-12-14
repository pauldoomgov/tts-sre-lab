# TTS SRE Lab

## Disclaimer

This repo contains various starting points for interview and learning exercises.

You should definitely not use anything in this repo for production or as an
example of good code, good engineering, or good taste.

## The Scenario

You have been employed by Presto Defecto LLC. as a Site Reliability Engineer.
Your initial task is to save  Presto Defecto's flagship service: Unstoppable Echo

Unstoppable Echo utilizes a polyglot micro-monolith architecture with a
fanout/in call structure.   At least that is what the consultancy said before
the initial VC funds ran out.

## The Problems

All components suffer from the same problems:

* Buggy code gets merged to `main`.
* There are tests, but...
* Deployment is done with `scp` and a prayer.
* Infrastructure is managed by mouse click so `prod`, `qa`, and `dev` are
  never the same.
* No one knows where to look when things go wrong.
* Things go wrong.  A lot.
* Few of the developers at Presto Defecto have heard of the OWASP top 10,
  but all are confident that there are no security vulnerabilities in
  Unstoppable Echo.
* It takes N-1 months for a new developer to come up to speed as there is no
  documentation.  (*Note - N is the number of months a given developer works
  at Presto Defecto before running away to a new job.)

With an IPO fast approaching, can you help productionalize Unstoppable Echo?

## The Wishlist

You have been handed a sticky note with a few lines scrawled on it.  Your new
manager says that it was made by the former SRE just before they were fired for
"not being a team player".  The manager grumbles "I dunno if this helps, but
here are a bunch of ideas the last SRE thought were important.  I don't see
the need, but whatever."

The note reads:

> todo or i can't take anymore
> * ci
>   * CI job that at least runs the tests
>   * functional tests so we know the code runs
>   * build step so we know what we deploy is the same - zip or Docker or something
> * cd
>   * automated deploy from `main`
>   * smoke test to make sure it worked
> * infra
>   * at least get compute instance and lb declared in code
>   * patch stuff
> * visibility
>   * logs should go somewhere
>   * tracing with opentracing or something - i have no idea what is going on
>   * monitoring... at least synthetics
> * config
>   * get secrets out of git and somewhere safe
>   * get all config passed in via envar
> * sec. scan
>   * code scanner like dependabot
>   * owasp zap scan in CI

## Your Challenge

One person can't do it all alone, but you will need to demo how things can be
made better.  You have been given a time limit of **three hours** to build your demo.

Your challenge:

* Fork this repo
* Select an area to focus on (ci, cd, infra, etc.)
* Create a proof of concept, in code
* Be ready to demo and walk through your code

Rules:
* GitHub, your local workstation, and free tier cloud services are allowed.  (No paid
services outside of free tier, please.)
* Time box your effort to **no more than three hours**.
* If you don't get something working that is OK!  Share what you have done.
* Application code can be modified **only** to add tooling or address configuration and build needs.  Implement tools to highlight security issues the application developers need to fix.
* Focus on **enabling the application developers** to address [The Problems](#the-problems).
