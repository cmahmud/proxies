# SyndProxy private pool

## Current pool

- Alive now: 1071
- Gold now: 415
- HTTP: 366 alive / 95 gold
- HTTPS: 253 alive / 34 gold
- SOCKS4: 179 alive / 119 gold
- SOCKS5: 273 alive / 167 gold

## Historical pool

- Discovered: 161919
- Ever alive: 31142
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
