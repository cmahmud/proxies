# SyndProxy private pool

## Current pool

- Alive now: 1071
- Gold now: 397
- HTTP: 330 alive / 71 gold
- HTTPS: 255 alive / 17 gold
- SOCKS4: 254 alive / 149 gold
- SOCKS5: 232 alive / 160 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20491
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
