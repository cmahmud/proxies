# SyndProxy private pool

## Current pool

- Alive now: 1245
- Gold now: 407
- HTTP: 402 alive / 93 gold
- HTTPS: 281 alive / 15 gold
- SOCKS4: 251 alive / 151 gold
- SOCKS5: 311 alive / 148 gold

## Historical pool

- Discovered: 131837
- Ever alive: 21143
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
