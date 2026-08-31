# SyndProxy validated proxy pool

## Current pool

- Alive now: 678
- Gold now: 469
- HTTP: 166 alive / 96 gold
- HTTPS: 118 alive / 37 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 220 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45310
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
