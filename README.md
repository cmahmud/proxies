# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 399
- HTTP: 81 alive / 54 gold
- HTTPS: 53 alive / 17 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36667
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
