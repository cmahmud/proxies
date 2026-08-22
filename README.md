# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 404
- HTTP: 344 alive / 87 gold
- HTTPS: 248 alive / 28 gold
- SOCKS4: 183 alive / 118 gold
- SOCKS5: 253 alive / 171 gold

## Historical pool

- Discovered: 166621
- Ever alive: 32454
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
