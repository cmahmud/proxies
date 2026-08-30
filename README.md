# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 424
- HTTP: 111 alive / 78 gold
- HTTPS: 43 alive / 20 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 196 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44495
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
