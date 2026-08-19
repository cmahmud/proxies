# SyndProxy private pool

## Current pool

- Alive now: 1136
- Gold now: 431
- HTTP: 394 alive / 125 gold
- HTTPS: 274 alive / 41 gold
- SOCKS4: 217 alive / 126 gold
- SOCKS5: 251 alive / 139 gold

## Historical pool

- Discovered: 117103
- Ever alive: 17137
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
