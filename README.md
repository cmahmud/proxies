# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 376
- HTTP: 328 alive / 87 gold
- HTTPS: 229 alive / 24 gold
- SOCKS4: 159 alive / 103 gold
- SOCKS5: 249 alive / 162 gold

## Historical pool

- Discovered: 166625
- Ever alive: 32457
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
