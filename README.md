# SyndProxy private pool

## Current pool

- Alive now: 867
- Gold now: 417
- HTTP: 240 alive / 90 gold
- HTTPS: 179 alive / 27 gold
- SOCKS4: 227 alive / 139 gold
- SOCKS5: 221 alive / 161 gold

## Historical pool

- Discovered: 151684
- Ever alive: 27710
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
