# SyndProxy private pool

## Current pool

- Alive now: 739
- Gold now: 381
- HTTP: 184 alive / 76 gold
- HTTPS: 135 alive / 18 gold
- SOCKS4: 219 alive / 150 gold
- SOCKS5: 201 alive / 137 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25937
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
