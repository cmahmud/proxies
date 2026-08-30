# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 424
- HTTP: 119 alive / 79 gold
- HTTPS: 57 alive / 19 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44327
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
