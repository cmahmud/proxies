# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 396
- HTTP: 94 alive / 55 gold
- HTTPS: 45 alive / 17 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36774
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
