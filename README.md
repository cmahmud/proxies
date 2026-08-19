# SyndProxy private pool

## Current pool

- Alive now: 1206
- Gold now: 395
- HTTP: 414 alive / 87 gold
- HTTPS: 250 alive / 17 gold
- SOCKS4: 239 alive / 145 gold
- SOCKS5: 303 alive / 146 gold

## Historical pool

- Discovered: 133968
- Ever alive: 21760
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
