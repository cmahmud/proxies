# SyndProxy private pool

## Current pool

- Alive now: 1089
- Gold now: 296
- HTTP: 397 alive / 60 gold
- HTTPS: 268 alive / 19 gold
- SOCKS4: 212 alive / 114 gold
- SOCKS5: 212 alive / 103 gold

## Historical pool

- Discovered: 109986
- Ever alive: 15591
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
