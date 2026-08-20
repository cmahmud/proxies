# SyndProxy private pool

## Current pool

- Alive now: 774
- Gold now: 411
- HTTP: 195 alive / 89 gold
- HTTPS: 152 alive / 21 gold
- SOCKS4: 201 alive / 146 gold
- SOCKS5: 226 alive / 155 gold

## Historical pool

- Discovered: 151068
- Ever alive: 27415
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
