# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 347
- HTTP: 299 alive / 51 gold
- HTTPS: 189 alive / 13 gold
- SOCKS4: 218 alive / 133 gold
- SOCKS5: 236 alive / 150 gold

## Historical pool

- Discovered: 107131
- Ever alive: 14909
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
