# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 403
- HTTP: 227 alive / 81 gold
- HTTPS: 248 alive / 20 gold
- SOCKS4: 206 alive / 150 gold
- SOCKS5: 215 alive / 152 gold

## Historical pool

- Discovered: 151073
- Ever alive: 27519
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
