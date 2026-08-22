# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 370
- HTTP: 249 alive / 82 gold
- HTTPS: 236 alive / 24 gold
- SOCKS4: 226 alive / 124 gold
- SOCKS5: 226 alive / 140 gold

## Historical pool

- Discovered: 164909
- Ever alive: 32119
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
