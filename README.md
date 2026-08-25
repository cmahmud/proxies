# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 399
- HTTP: 71 alive / 58 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36523
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
