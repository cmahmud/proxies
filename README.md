# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 417
- HTTP: 370 alive / 95 gold
- HTTPS: 251 alive / 36 gold
- SOCKS4: 184 alive / 119 gold
- SOCKS5: 270 alive / 167 gold

## Historical pool

- Discovered: 161919
- Ever alive: 31141
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
