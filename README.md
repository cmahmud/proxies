# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 378
- HTTP: 95 alive / 51 gold
- HTTPS: 43 alive / 9 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33429
- Ever gold: 1237

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
