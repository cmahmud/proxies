# SyndProxy private pool

## Current pool

- Alive now: 698
- Gold now: 204
- HTTP: 199 alive / 26 gold
- HTTPS: 102 alive / 7 gold
- SOCKS4: 199 alive / 100 gold
- SOCKS5: 198 alive / 71 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8346
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
