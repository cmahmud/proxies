# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 428
- HTTP: 119 alive / 78 gold
- HTTPS: 58 alive / 24 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44543
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
