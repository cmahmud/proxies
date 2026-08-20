# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 360
- HTTP: 259 alive / 79 gold
- HTTPS: 206 alive / 21 gold
- SOCKS4: 192 alive / 134 gold
- SOCKS5: 190 alive / 126 gold

## Historical pool

- Discovered: 149491
- Ever alive: 26578
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
