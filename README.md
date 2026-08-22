# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 393
- HTTP: 206 alive / 87 gold
- HTTPS: 156 alive / 30 gold
- SOCKS4: 193 alive / 119 gold
- SOCKS5: 224 alive / 157 gold

## Historical pool

- Discovered: 163856
- Ever alive: 31951
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
