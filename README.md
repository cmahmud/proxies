# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 400
- HTTP: 75 alive / 58 gold
- HTTPS: 42 alive / 13 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36531
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
