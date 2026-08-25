# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 399
- HTTP: 84 alive / 58 gold
- HTTPS: 63 alive / 13 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36417
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
