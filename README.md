# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 423
- HTTP: 109 alive / 77 gold
- HTTPS: 47 alive / 25 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49476
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
