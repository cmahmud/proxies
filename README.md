# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 460
- HTTP: 137 alive / 87 gold
- HTTPS: 114 alive / 35 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46722
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
