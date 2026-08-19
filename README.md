# SyndProxy private pool

## Current pool

- Alive now: 1436
- Gold now: 416
- HTTP: 540 alive / 86 gold
- HTTPS: 362 alive / 17 gold
- SOCKS4: 256 alive / 157 gold
- SOCKS5: 278 alive / 156 gold

## Historical pool

- Discovered: 131814
- Ever alive: 20852
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
