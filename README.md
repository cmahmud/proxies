# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 442
- HTTP: 137 alive / 81 gold
- HTTPS: 110 alive / 30 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 213 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45427
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
