# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 435
- HTTP: 126 alive / 78 gold
- HTTPS: 90 alive / 27 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 202 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45460
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
