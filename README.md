# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 399
- HTTP: 74 alive / 58 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36529
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
