# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 446
- HTTP: 119 alive / 79 gold
- HTTPS: 140 alive / 35 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44694
- Ever gold: 1410

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
