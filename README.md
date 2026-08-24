# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 391
- HTTP: 140 alive / 54 gold
- HTTPS: 35 alive / 13 gold
- SOCKS4: 178 alive / 156 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33625
- Ever gold: 1244

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
