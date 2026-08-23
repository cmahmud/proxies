# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 388
- HTTP: 106 alive / 61 gold
- HTTPS: 44 alive / 14 gold
- SOCKS4: 162 alive / 154 gold
- SOCKS5: 177 alive / 159 gold

## Historical pool

- Discovered: 175416
- Ever alive: 33125
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
