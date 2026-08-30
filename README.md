# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 448
- HTTP: 113 alive / 81 gold
- HTTPS: 133 alive / 38 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44732
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
