# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 468
- HTTP: 126 alive / 96 gold
- HTTPS: 124 alive / 39 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44844
- Ever gold: 1415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
