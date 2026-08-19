# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 362
- HTTP: 344 alive / 67 gold
- HTTPS: 192 alive / 16 gold
- SOCKS4: 235 alive / 156 gold
- SOCKS5: 227 alive / 123 gold

## Historical pool

- Discovered: 111009
- Ever alive: 16109
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
