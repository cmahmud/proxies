# SyndProxy private pool

## Current pool

- Alive now: 693
- Gold now: 383
- HTTP: 175 alive / 76 gold
- HTTPS: 98 alive / 17 gold
- SOCKS4: 212 alive / 149 gold
- SOCKS5: 208 alive / 141 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25946
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
