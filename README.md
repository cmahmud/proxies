# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 461
- HTTP: 119 alive / 92 gold
- HTTPS: 114 alive / 34 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44893
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
