# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 425
- HTTP: 218 alive / 94 gold
- HTTPS: 148 alive / 29 gold
- SOCKS4: 189 alive / 137 gold
- SOCKS5: 224 alive / 165 gold

## Historical pool

- Discovered: 162702
- Ever alive: 31454
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
