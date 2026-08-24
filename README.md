# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 382
- HTTP: 103 alive / 58 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 178 alive / 158 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33437
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
