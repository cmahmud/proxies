# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 392
- HTTP: 292 alive / 76 gold
- HTTPS: 206 alive / 13 gold
- SOCKS4: 253 alive / 151 gold
- SOCKS5: 245 alive / 152 gold

## Historical pool

- Discovered: 129305
- Ever alive: 20397
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
