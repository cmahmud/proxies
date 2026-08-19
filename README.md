# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 397
- HTTP: 324 alive / 72 gold
- HTTPS: 226 alive / 16 gold
- SOCKS4: 255 alive / 148 gold
- SOCKS5: 235 alive / 161 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20470
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
