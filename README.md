# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 405
- HTTP: 93 alive / 59 gold
- HTTPS: 48 alive / 18 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36702
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
