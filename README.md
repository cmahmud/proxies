# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 393
- HTTP: 75 alive / 51 gold
- HTTPS: 37 alive / 14 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36580
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
