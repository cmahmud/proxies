# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 376
- HTTP: 82 alive / 44 gold
- HTTPS: 41 alive / 11 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 192 alive / 162 gold

## Historical pool

- Discovered: 172323
- Ever alive: 32984
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
