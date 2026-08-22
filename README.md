# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 411
- HTTP: 303 alive / 92 gold
- HTTPS: 243 alive / 28 gold
- SOCKS4: 190 alive / 120 gold
- SOCKS5: 255 alive / 171 gold

## Historical pool

- Discovered: 166621
- Ever alive: 32454
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
