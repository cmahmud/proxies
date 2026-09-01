# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 471
- HTTP: 147 alive / 93 gold
- HTTPS: 122 alive / 41 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 198 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46938
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
