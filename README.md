# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 405
- HTTP: 91 alive / 63 gold
- HTTPS: 60 alive / 14 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36426
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
