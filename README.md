# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 448
- HTTP: 113 alive / 85 gold
- HTTPS: 69 alive / 33 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 201 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44588
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
