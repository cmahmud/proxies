# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 393
- HTTP: 79 alive / 50 gold
- HTTPS: 39 alive / 13 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36554
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
