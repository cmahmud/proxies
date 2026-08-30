# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 419
- HTTP: 111 alive / 70 gold
- HTTPS: 60 alive / 22 gold
- SOCKS4: 162 alive / 160 gold
- SOCKS5: 195 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44465
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
