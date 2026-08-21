# SyndProxy private pool

## Current pool

- Alive now: 1168
- Gold now: 404
- HTTP: 441 alive / 101 gold
- HTTPS: 237 alive / 24 gold
- SOCKS4: 227 alive / 131 gold
- SOCKS5: 263 alive / 148 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27955
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
