# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 392
- HTTP: 73 alive / 49 gold
- HTTPS: 42 alive / 13 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36551
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
