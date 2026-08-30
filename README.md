# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 446
- HTTP: 133 alive / 88 gold
- HTTPS: 74 alive / 34 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 197 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44280
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
