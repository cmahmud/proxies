# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 281
- HTTP: 320 alive / 38 gold
- HTTPS: 204 alive / 10 gold
- SOCKS4: 219 alive / 140 gold
- SOCKS5: 161 alive / 93 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13934
- Ever gold: 433

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
