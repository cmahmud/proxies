# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 372
- HTTP: 306 alive / 83 gold
- HTTPS: 246 alive / 27 gold
- SOCKS4: 178 alive / 127 gold
- SOCKS5: 226 alive / 135 gold

## Historical pool

- Discovered: 166948
- Ever alive: 32484
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
