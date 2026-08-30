# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 462
- HTTP: 120 alive / 93 gold
- HTTPS: 118 alive / 34 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 203 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44893
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
