# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 460
- HTTP: 120 alive / 88 gold
- HTTPS: 120 alive / 35 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 185 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46725
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
