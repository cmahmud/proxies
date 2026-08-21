# SyndProxy private pool

## Current pool

- Alive now: 1086
- Gold now: 401
- HTTP: 374 alive / 98 gold
- HTTPS: 221 alive / 21 gold
- SOCKS4: 231 alive / 132 gold
- SOCKS5: 260 alive / 150 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27950
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
