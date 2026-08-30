# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 462
- HTTP: 137 alive / 95 gold
- HTTPS: 117 alive / 38 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 201 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44832
- Ever gold: 1415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
