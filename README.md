# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 457
- HTTP: 123 alive / 83 gold
- HTTPS: 124 alive / 35 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 186 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46707
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
