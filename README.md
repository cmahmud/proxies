# SyndProxy private pool

## Current pool

- Alive now: 1161
- Gold now: 401
- HTTP: 419 alive / 100 gold
- HTTPS: 247 alive / 25 gold
- SOCKS4: 227 alive / 130 gold
- SOCKS5: 268 alive / 146 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27955
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
