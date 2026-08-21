# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 345
- HTTP: 248 alive / 75 gold
- HTTPS: 166 alive / 21 gold
- SOCKS4: 205 alive / 119 gold
- SOCKS5: 217 alive / 130 gold

## Historical pool

- Discovered: 157604
- Ever alive: 29779
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
