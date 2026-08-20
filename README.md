# SyndProxy private pool

## Current pool

- Alive now: 1326
- Gold now: 603
- HTTP: 498 alive / 203 gold
- HTTPS: 363 alive / 101 gold
- SOCKS4: 220 alive / 146 gold
- SOCKS5: 245 alive / 153 gold

## Historical pool

- Discovered: 138953
- Ever alive: 23398
- Ever gold: 920

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
