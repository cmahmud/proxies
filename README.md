# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 421
- HTTP: 102 alive / 77 gold
- HTTPS: 45 alive / 23 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49449
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
