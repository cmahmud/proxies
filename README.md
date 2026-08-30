# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 428
- HTTP: 114 alive / 79 gold
- HTTPS: 50 alive / 23 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44517
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
