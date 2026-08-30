# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 451
- HTTP: 107 alive / 84 gold
- HTTPS: 45 alive / 30 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 185 alive / 175 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43683
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
