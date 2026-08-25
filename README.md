# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 404
- HTTP: 89 alive / 58 gold
- HTTPS: 46 alive / 18 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36702
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
