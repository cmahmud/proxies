# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 447
- HTTP: 141 alive / 87 gold
- HTTPS: 82 alive / 34 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 209 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44222
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
