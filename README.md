# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 382
- HTTP: 311 alive / 82 gold
- HTTPS: 192 alive / 23 gold
- SOCKS4: 224 alive / 139 gold
- SOCKS5: 241 alive / 138 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29714
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
