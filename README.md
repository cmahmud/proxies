# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 397
- HTTP: 305 alive / 83 gold
- HTTPS: 192 alive / 20 gold
- SOCKS4: 228 alive / 149 gold
- SOCKS5: 251 alive / 145 gold

## Historical pool

- Discovered: 158238
- Ever alive: 29984
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
