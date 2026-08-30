# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 440
- HTTP: 131 alive / 87 gold
- HTTPS: 91 alive / 28 gold
- SOCKS4: 162 alive / 159 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44286
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
