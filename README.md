# SyndProxy private pool

## Current pool

- Alive now: 1124
- Gold now: 401
- HTTP: 358 alive / 74 gold
- HTTPS: 239 alive / 13 gold
- SOCKS4: 275 alive / 157 gold
- SOCKS5: 252 alive / 157 gold

## Historical pool

- Discovered: 131118
- Ever alive: 20679
- Ever gold: 872

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
