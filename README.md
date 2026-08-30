# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 428
- HTTP: 124 alive / 86 gold
- HTTPS: 97 alive / 31 gold
- SOCKS4: 162 alive / 152 gold
- SOCKS5: 199 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44017
- Ever gold: 1388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
