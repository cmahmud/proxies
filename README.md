# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 460
- HTTP: 122 alive / 90 gold
- HTTPS: 126 alive / 36 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46709
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
