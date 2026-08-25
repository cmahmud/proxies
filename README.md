# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 394
- HTTP: 79 alive / 55 gold
- HTTPS: 43 alive / 13 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36502
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
