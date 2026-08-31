# SyndProxy validated proxy pool

## Current pool

- Alive now: 697
- Gold now: 460
- HTTP: 131 alive / 90 gold
- HTTPS: 151 alive / 34 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 236 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45821
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
