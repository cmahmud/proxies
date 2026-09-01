# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 464
- HTTP: 124 alive / 87 gold
- HTTPS: 104 alive / 40 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46970
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
