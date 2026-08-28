# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 391
- HTTP: 78 alive / 58 gold
- HTTPS: 61 alive / 12 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 174 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42818
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
