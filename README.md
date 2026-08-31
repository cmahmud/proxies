# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 447
- HTTP: 111 alive / 85 gold
- HTTPS: 68 alive / 29 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45566
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
