# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 391
- HTTP: 97 alive / 56 gold
- HTTPS: 47 alive / 14 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36769
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
