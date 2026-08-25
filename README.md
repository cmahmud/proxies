# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 412
- HTTP: 87 alive / 65 gold
- HTTPS: 48 alive / 19 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36750
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
