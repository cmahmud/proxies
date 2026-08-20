# SyndProxy private pool

## Current pool

- Alive now: 1425
- Gold now: 623
- HTTP: 511 alive / 207 gold
- HTTPS: 426 alive / 115 gold
- SOCKS4: 239 alive / 144 gold
- SOCKS5: 249 alive / 157 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24040
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
