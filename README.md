# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 448
- HTTP: 124 alive / 80 gold
- HTTPS: 85 alive / 35 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 202 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45597
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
