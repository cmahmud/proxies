# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 299
- HTTP: 365 alive / 60 gold
- HTTPS: 256 alive / 19 gold
- SOCKS4: 209 alive / 115 gold
- SOCKS5: 211 alive / 105 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15592
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
