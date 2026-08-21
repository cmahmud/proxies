# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 403
- HTTP: 403 alive / 102 gold
- HTTPS: 296 alive / 30 gold
- SOCKS4: 230 alive / 152 gold
- SOCKS5: 227 alive / 119 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30326
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
