# SyndProxy private pool

## Current pool

- Alive now: 1122
- Gold now: 415
- HTTP: 371 alive / 92 gold
- HTTPS: 246 alive / 20 gold
- SOCKS4: 227 alive / 143 gold
- SOCKS5: 278 alive / 160 gold

## Historical pool

- Discovered: 136195
- Ever alive: 22306
- Ever gold: 895

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
