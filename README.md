# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 426
- HTTP: 121 alive / 80 gold
- HTTPS: 58 alive / 19 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44327
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
