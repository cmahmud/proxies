# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 378
- HTTP: 95 alive / 47 gold
- HTTPS: 44 alive / 10 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 180 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33537
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
