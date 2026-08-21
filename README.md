# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 402
- HTTP: 304 alive / 106 gold
- HTTPS: 223 alive / 29 gold
- SOCKS4: 204 alive / 147 gold
- SOCKS5: 207 alive / 120 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28473
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
