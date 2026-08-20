# SyndProxy private pool

## Current pool

- Alive now: 761
- Gold now: 381
- HTTP: 200 alive / 80 gold
- HTTPS: 150 alive / 19 gold
- SOCKS4: 219 alive / 151 gold
- SOCKS5: 192 alive / 131 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25937
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
