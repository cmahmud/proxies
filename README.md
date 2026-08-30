# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 431
- HTTP: 150 alive / 88 gold
- HTTPS: 95 alive / 31 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 208 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44012
- Ever gold: 1388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
