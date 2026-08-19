# SyndProxy private pool

## Current pool

- Alive now: 1356
- Gold now: 409
- HTTP: 453 alive / 80 gold
- HTTPS: 332 alive / 16 gold
- SOCKS4: 248 alive / 157 gold
- SOCKS5: 323 alive / 156 gold

## Historical pool

- Discovered: 134532
- Ever alive: 21954
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
