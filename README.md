# SyndProxy private pool

## Current pool

- Alive now: 1421
- Gold now: 569
- HTTP: 473 alive / 192 gold
- HTTPS: 397 alive / 90 gold
- SOCKS4: 234 alive / 151 gold
- SOCKS5: 317 alive / 136 gold

## Historical pool

- Discovered: 140459
- Ever alive: 23610
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
