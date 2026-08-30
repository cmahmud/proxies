# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 449
- HTTP: 124 alive / 92 gold
- HTTPS: 70 alive / 34 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 205 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44237
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
