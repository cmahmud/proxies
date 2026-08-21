# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 406
- HTTP: 224 alive / 88 gold
- HTTPS: 95 alive / 17 gold
- SOCKS4: 222 alive / 149 gold
- SOCKS5: 238 alive / 152 gold

## Historical pool

- Discovered: 155739
- Ever alive: 29287
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
