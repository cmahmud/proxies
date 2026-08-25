# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 403
- HTTP: 81 alive / 58 gold
- HTTPS: 58 alive / 14 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 180 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36454
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
