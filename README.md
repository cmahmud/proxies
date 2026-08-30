# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 451
- HTTP: 144 alive / 92 gold
- HTTPS: 98 alive / 35 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 198 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44193
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
