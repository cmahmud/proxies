# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 399
- HTTP: 90 alive / 55 gold
- HTTPS: 42 alive / 18 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36762
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
