# SyndProxy private pool

## Current pool

- Alive now: 703
- Gold now: 381
- HTTP: 177 alive / 78 gold
- HTTPS: 117 alive / 17 gold
- SOCKS4: 212 alive / 149 gold
- SOCKS5: 197 alive / 137 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25944
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
