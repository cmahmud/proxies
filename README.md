# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 394
- HTTP: 94 alive / 64 gold
- HTTPS: 44 alive / 15 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 183 alive / 160 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48139
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
