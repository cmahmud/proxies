# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 447
- HTTP: 110 alive / 84 gold
- HTTPS: 70 alive / 33 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 208 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44588
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
