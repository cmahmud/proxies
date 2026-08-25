# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 408
- HTTP: 91 alive / 64 gold
- HTTPS: 62 alive / 15 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36427
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
