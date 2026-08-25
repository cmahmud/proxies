# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 408
- HTTP: 87 alive / 61 gold
- HTTPS: 60 alive / 18 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36694
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
