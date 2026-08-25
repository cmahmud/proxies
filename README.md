# SyndProxy validated proxy pool

## Current pool

- Alive now: 456
- Gold now: 400
- HTTP: 73 alive / 57 gold
- HTTPS: 37 alive / 13 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 179 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36513
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
