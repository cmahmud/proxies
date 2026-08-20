# SyndProxy private pool

## Current pool

- Alive now: 688
- Gold now: 373
- HTTP: 172 alive / 83 gold
- HTTPS: 102 alive / 18 gold
- SOCKS4: 201 alive / 137 gold
- SOCKS5: 213 alive / 135 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25948
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
