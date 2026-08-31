# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 449
- HTTP: 124 alive / 80 gold
- HTTPS: 90 alive / 36 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45598
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
