# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 408
- HTTP: 92 alive / 61 gold
- HTTPS: 64 alive / 18 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36365
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
