# SyndProxy private pool

## Current pool

- Alive now: 1225
- Gold now: 417
- HTTP: 396 alive / 88 gold
- HTTPS: 308 alive / 24 gold
- SOCKS4: 229 alive / 146 gold
- SOCKS5: 292 alive / 159 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22378
- Ever gold: 898

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
