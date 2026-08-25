# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 402
- HTTP: 87 alive / 57 gold
- HTTPS: 44 alive / 18 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36702
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
