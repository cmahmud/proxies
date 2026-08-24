# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 378
- HTTP: 99 alive / 52 gold
- HTTPS: 34 alive / 10 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 188 alive / 161 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33424
- Ever gold: 1237

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
