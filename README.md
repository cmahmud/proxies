# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 423
- HTTP: 112 alive / 77 gold
- HTTPS: 44 alive / 19 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 199 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44495
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
