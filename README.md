# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 380
- HTTP: 107 alive / 48 gold
- HTTPS: 34 alive / 10 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33536
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
