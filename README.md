# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 426
- HTTP: 120 alive / 77 gold
- HTTPS: 58 alive / 24 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44543
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
