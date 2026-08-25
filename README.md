# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 394
- HTTP: 76 alive / 53 gold
- HTTPS: 53 alive / 12 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36542
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
