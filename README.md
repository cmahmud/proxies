# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 444
- HTTP: 146 alive / 80 gold
- HTTPS: 99 alive / 30 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 218 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45447
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
