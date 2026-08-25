# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 399
- HTTP: 73 alive / 57 gold
- HTTPS: 44 alive / 13 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36531
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
