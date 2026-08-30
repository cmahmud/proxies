# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 469
- HTTP: 128 alive / 96 gold
- HTTPS: 121 alive / 40 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44845
- Ever gold: 1415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
