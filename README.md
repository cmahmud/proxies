# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 415
- HTTP: 368 alive / 107 gold
- HTTPS: 206 alive / 29 gold
- SOCKS4: 207 alive / 133 gold
- SOCKS5: 231 alive / 146 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30627
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
