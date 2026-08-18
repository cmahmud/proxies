# SyndProxy private pool

## Current pool

- Alive now: 761
- Gold now: 203
- HTTP: 214 alive / 24 gold
- HTTPS: 110 alive / 7 gold
- SOCKS4: 213 alive / 100 gold
- SOCKS5: 224 alive / 72 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8346
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
