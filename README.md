# SyndProxy private pool

## Current pool

- Alive now: 903
- Gold now: 415
- HTTP: 259 alive / 95 gold
- HTTPS: 189 alive / 27 gold
- SOCKS4: 200 alive / 136 gold
- SOCKS5: 255 alive / 157 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29067
- Ever gold: 1122

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
