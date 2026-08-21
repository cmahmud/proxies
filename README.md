# SyndProxy private pool

## Current pool

- Alive now: 936
- Gold now: 414
- HTTP: 284 alive / 89 gold
- HTTPS: 215 alive / 21 gold
- SOCKS4: 210 alive / 155 gold
- SOCKS5: 227 alive / 149 gold

## Historical pool

- Discovered: 158244
- Ever alive: 30041
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
