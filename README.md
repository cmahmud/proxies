# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 459
- HTTP: 121 alive / 89 gold
- HTTPS: 128 alive / 36 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46709
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
