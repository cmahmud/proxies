# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 465
- HTTP: 136 alive / 94 gold
- HTTPS: 112 alive / 37 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 205 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44850
- Ever gold: 1416

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
