# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 392
- HTTP: 76 alive / 58 gold
- HTTPS: 57 alive / 12 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 175 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42818
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
