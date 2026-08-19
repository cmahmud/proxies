# SyndProxy private pool

## Current pool

- Alive now: 1447
- Gold now: 393
- HTTP: 499 alive / 91 gold
- HTTPS: 352 alive / 19 gold
- SOCKS4: 264 alive / 129 gold
- SOCKS5: 332 alive / 154 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22028
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
