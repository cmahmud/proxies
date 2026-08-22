# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 370
- HTTP: 360 alive / 79 gold
- HTTPS: 212 alive / 25 gold
- SOCKS4: 207 alive / 136 gold
- SOCKS5: 220 alive / 130 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32360
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
