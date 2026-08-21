# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 349
- HTTP: 230 alive / 75 gold
- HTTPS: 158 alive / 19 gold
- SOCKS4: 205 alive / 124 gold
- SOCKS5: 186 alive / 131 gold

## Historical pool

- Discovered: 157663
- Ever alive: 29790
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
