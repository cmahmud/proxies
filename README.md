# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 408
- HTTP: 86 alive / 58 gold
- HTTPS: 52 alive / 19 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36716
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
