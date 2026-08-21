# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 399
- HTTP: 366 alive / 86 gold
- HTTPS: 192 alive / 23 gold
- SOCKS4: 204 alive / 129 gold
- SOCKS5: 256 alive / 161 gold

## Historical pool

- Discovered: 157414
- Ever alive: 29710
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
