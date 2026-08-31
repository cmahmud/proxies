# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 443
- HTTP: 122 alive / 81 gold
- HTTPS: 94 alive / 27 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 201 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45461
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
