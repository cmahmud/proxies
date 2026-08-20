# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 411
- HTTP: 190 alive / 87 gold
- HTTPS: 149 alive / 25 gold
- SOCKS4: 217 alive / 154 gold
- SOCKS5: 223 alive / 145 gold

## Historical pool

- Discovered: 149523
- Ever alive: 26992
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
