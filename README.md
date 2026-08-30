# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 425
- HTTP: 121 alive / 79 gold
- HTTPS: 60 alive / 19 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 194 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44327
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
