# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 436
- HTTP: 374 alive / 107 gold
- HTTPS: 233 alive / 28 gold
- SOCKS4: 208 alive / 134 gold
- SOCKS5: 253 alive / 167 gold

## Historical pool

- Discovered: 160212
- Ever alive: 30655
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
