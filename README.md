# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 431
- HTTP: 102 alive / 81 gold
- HTTPS: 65 alive / 24 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44528
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
