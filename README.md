# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 390
- HTTP: 273 alive / 89 gold
- HTTPS: 220 alive / 22 gold
- SOCKS4: 183 alive / 134 gold
- SOCKS5: 206 alive / 145 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27882
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
