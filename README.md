# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 407
- HTTP: 82 alive / 59 gold
- HTTPS: 53 alive / 18 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36702
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
