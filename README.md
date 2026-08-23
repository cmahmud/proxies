# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 362
- HTTP: 95 alive / 36 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 179 alive / 159 gold

## Historical pool

- Discovered: 171600
- Ever alive: 32940
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
