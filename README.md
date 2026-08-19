# SyndProxy private pool

## Current pool

- Alive now: 1285
- Gold now: 389
- HTTP: 439 alive / 92 gold
- HTTPS: 296 alive / 19 gold
- SOCKS4: 242 alive / 137 gold
- SOCKS5: 308 alive / 141 gold

## Historical pool

- Discovered: 133964
- Ever alive: 21650
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
