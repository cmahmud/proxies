# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 446
- HTTP: 119 alive / 81 gold
- HTTPS: 126 alive / 35 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44723
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
