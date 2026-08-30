# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 448
- HTTP: 129 alive / 82 gold
- HTTPS: 151 alive / 35 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44708
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
