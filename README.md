# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 457
- HTTP: 313 alive / 100 gold
- HTTPS: 203 alive / 37 gold
- SOCKS4: 202 alive / 149 gold
- SOCKS5: 273 alive / 171 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28696
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
