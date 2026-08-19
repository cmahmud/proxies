# SyndProxy private pool

## Current pool

- Alive now: 1119
- Gold now: 498
- HTTP: 382 alive / 123 gold
- HTTPS: 245 alive / 73 gold
- SOCKS4: 232 alive / 150 gold
- SOCKS5: 260 alive / 152 gold

## Historical pool

- Discovered: 114411
- Ever alive: 17013
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
