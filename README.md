# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 227
- HTTP: 266 alive / 30 gold
- HTTPS: 101 alive / 8 gold
- SOCKS4: 204 alive / 116 gold
- SOCKS5: 208 alive / 73 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9309
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
