# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 426
- HTTP: 105 alive / 73 gold
- HTTPS: 63 alive / 28 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44350
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
