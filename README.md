# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 415
- HTTP: 220 alive / 82 gold
- HTTPS: 143 alive / 25 gold
- SOCKS4: 214 alive / 143 gold
- SOCKS5: 259 alive / 165 gold

## Historical pool

- Discovered: 155796
- Ever alive: 29340
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
