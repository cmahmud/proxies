# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 451
- HTTP: 126 alive / 82 gold
- HTTPS: 143 alive / 39 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44747
- Ever gold: 1412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
