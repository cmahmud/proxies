# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 430
- HTTP: 100 alive / 77 gold
- HTTPS: 56 alive / 25 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 203 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44557
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
