# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 394
- HTTP: 306 alive / 87 gold
- HTTPS: 224 alive / 23 gold
- SOCKS4: 227 alive / 135 gold
- SOCKS5: 243 alive / 149 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32097
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
