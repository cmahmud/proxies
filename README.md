# SyndProxy private pool

## Current pool

- Alive now: 1219
- Gold now: 430
- HTTP: 438 alive / 101 gold
- HTTPS: 330 alive / 29 gold
- SOCKS4: 211 alive / 139 gold
- SOCKS5: 240 alive / 161 gold

## Historical pool

- Discovered: 159281
- Ever alive: 30415
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
