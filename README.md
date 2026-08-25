# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 407
- HTTP: 89 alive / 64 gold
- HTTPS: 60 alive / 15 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36427
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
