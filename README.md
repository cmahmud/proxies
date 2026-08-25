# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 399
- HTTP: 88 alive / 58 gold
- HTTPS: 45 alive / 16 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36776
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
