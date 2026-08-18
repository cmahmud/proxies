# SyndProxy private pool

## Current pool

- Alive now: 909
- Gold now: 344
- HTTP: 296 alive / 49 gold
- HTTPS: 186 alive / 14 gold
- SOCKS4: 211 alive / 133 gold
- SOCKS5: 216 alive / 148 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14916
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
