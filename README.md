# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 333
- HTTP: 309 alive / 83 gold
- HTTPS: 207 alive / 20 gold
- SOCKS4: 199 alive / 141 gold
- SOCKS5: 196 alive / 89 gold

## Historical pool

- Discovered: 167096
- Ever alive: 32492
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
