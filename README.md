# SyndProxy private pool

## Current pool

- Alive now: 1089
- Gold now: 529
- HTTP: 405 alive / 156 gold
- HTTPS: 275 alive / 90 gold
- SOCKS4: 201 alive / 138 gold
- SOCKS5: 208 alive / 145 gold

## Historical pool

- Discovered: 127355
- Ever alive: 19886
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
