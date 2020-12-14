# TTS SRE Lab

## Disclaimer

This repo contains various starting points for interview and learning excercises.

You should definiately not use anything in this repo for production or as an
example of good code, good engineering, or good taste.

## The Scenario

You have been employed by Presto Defecto LLC. as a Site Reliability Engineer.
Your initial task is to save  Presto Defecto's flagship service: Unstoppable Echo

Unstoppable Echo is a monolith but has been re-implemented in four languages.

All implementations suffer from the same problems:

* Buggy code gets merged to `main`.
* Deployment is done with `scp` and a prayer.
* No one knows where to look when things go wrong.
* Things go wrong.  A lot.
* None of the developers at Presto Defecto have heard of the OWASP top 10,
  but all are confident that there are no security vulnerabilities in
  Unstoppable Echo.
* It takes N-1 months for a new developer to come up to speed as there is no
  documentation.  (*Note - N is the number of months a given developer works
  at Presto Defecto before running away to a new job.)

With the IPO fast approaching, can you help productionalize Unstoppable Echo?
