# SyndProxy private pool

## Current pool

- Alive now: 1425
- Gold now: 589
- HTTP: 500 alive / 195 gold
- HTTPS: 442 alive / 92 gold
- SOCKS4: 239 alive / 145 gold
- SOCKS5: 244 alive / 157 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24050
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
