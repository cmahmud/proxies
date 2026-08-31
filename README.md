# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 447
- HTTP: 122 alive / 82 gold
- HTTPS: 118 alive / 32 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45642
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
