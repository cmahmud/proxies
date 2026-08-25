# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 399
- HTTP: 85 alive / 54 gold
- HTTPS: 43 alive / 17 gold
- SOCKS4: 182 alive / 160 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36674
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
