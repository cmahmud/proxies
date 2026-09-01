# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 462
- HTTP: 123 alive / 89 gold
- HTTPS: 130 alive / 35 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46708
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
