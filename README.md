# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 411
- HTTP: 92 alive / 60 gold
- HTTPS: 45 alive / 18 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 184 alive / 173 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36728
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
