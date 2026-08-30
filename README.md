# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 427
- HTTP: 116 alive / 79 gold
- HTTPS: 65 alive / 24 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 207 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44337
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
