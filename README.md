# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 472
- HTTP: 122 alive / 97 gold
- HTTPS: 112 alive / 41 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44845
- Ever gold: 1416

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
