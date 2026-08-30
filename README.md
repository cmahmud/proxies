# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 444
- HTTP: 122 alive / 89 gold
- HTTPS: 77 alive / 31 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44288
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
