# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 396
- HTTP: 82 alive / 58 gold
- HTTPS: 44 alive / 12 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36504
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
