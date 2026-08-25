# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 403
- HTTP: 105 alive / 60 gold
- HTTPS: 51 alive / 18 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36802
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
