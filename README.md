# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 442
- HTTP: 113 alive / 77 gold
- HTTPS: 132 alive / 34 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44657
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
