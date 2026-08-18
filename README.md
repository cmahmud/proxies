# SyndProxy private pool

## Current pool

- Alive now: 673
- Gold now: 207
- HTTP: 174 alive / 28 gold
- HTTPS: 102 alive / 7 gold
- SOCKS4: 202 alive / 100 gold
- SOCKS5: 195 alive / 72 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8359
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
