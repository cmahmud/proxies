# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 441
- HTTP: 134 alive / 81 gold
- HTTPS: 109 alive / 29 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 213 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45427
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
