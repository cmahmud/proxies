# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 410
- HTTP: 299 alive / 93 gold
- HTTPS: 231 alive / 28 gold
- SOCKS4: 189 alive / 119 gold
- SOCKS5: 244 alive / 170 gold

## Historical pool

- Discovered: 166621
- Ever alive: 32454
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
