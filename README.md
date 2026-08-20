# SyndProxy private pool

## Current pool

- Alive now: 729
- Gold now: 381
- HTTP: 190 alive / 77 gold
- HTTPS: 123 alive / 18 gold
- SOCKS4: 214 alive / 150 gold
- SOCKS5: 202 alive / 136 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25944
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
