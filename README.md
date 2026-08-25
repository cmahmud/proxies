# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 407
- HTTP: 79 alive / 62 gold
- HTTPS: 46 alive / 17 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36751
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
