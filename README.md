# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 382
- HTTP: 110 alive / 57 gold
- HTTPS: 38 alive / 10 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 179 alive / 160 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33438
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
