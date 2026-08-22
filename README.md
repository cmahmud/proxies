# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 415
- HTTP: 307 alive / 89 gold
- HTTPS: 240 alive / 30 gold
- SOCKS4: 215 alive / 143 gold
- SOCKS5: 248 alive / 153 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32081
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
