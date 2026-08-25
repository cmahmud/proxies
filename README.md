# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 398
- HTTP: 78 alive / 57 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 179 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36511
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
