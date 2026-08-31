# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 439
- HTTP: 122 alive / 78 gold
- HTTPS: 74 alive / 27 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45561
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
