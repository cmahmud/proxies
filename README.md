# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 437
- HTTP: 140 alive / 82 gold
- HTTPS: 102 alive / 25 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34576
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
