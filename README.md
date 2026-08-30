# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 421
- HTTP: 136 alive / 81 gold
- HTTPS: 83 alive / 29 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 215 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43981
- Ever gold: 1381

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
