# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 424
- HTTP: 118 alive / 72 gold
- HTTPS: 71 alive / 27 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 199 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44347
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
