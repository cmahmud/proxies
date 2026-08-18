# SyndProxy private pool

## Current pool

- Alive now: 640
- Gold now: 213
- HTTP: 168 alive / 30 gold
- HTTPS: 101 alive / 7 gold
- SOCKS4: 188 alive / 102 gold
- SOCKS5: 183 alive / 74 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8359
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
