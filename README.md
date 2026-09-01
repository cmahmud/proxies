# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 460
- HTTP: 118 alive / 88 gold
- HTTPS: 118 alive / 35 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 187 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46725
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
