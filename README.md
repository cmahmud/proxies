# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 398
- HTTP: 73 alive / 58 gold
- HTTPS: 47 alive / 12 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36528
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
