# SyndProxy private pool

## Current pool

- Alive now: 898
- Gold now: 397
- HTTP: 233 alive / 78 gold
- HTTPS: 255 alive / 20 gold
- SOCKS4: 195 alive / 149 gold
- SOCKS5: 215 alive / 150 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26504
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
