# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 442
- HTTP: 118 alive / 76 gold
- HTTPS: 132 alive / 35 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44661
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
