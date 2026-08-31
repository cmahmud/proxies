# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 437
- HTTP: 117 alive / 76 gold
- HTTPS: 82 alive / 28 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 200 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45461
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
