# SyndProxy private pool

## Current pool

- Alive now: 1099
- Gold now: 408
- HTTP: 392 alive / 106 gold
- HTTPS: 244 alive / 27 gold
- SOCKS4: 224 alive / 133 gold
- SOCKS5: 239 alive / 142 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30623
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
