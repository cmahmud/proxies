# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 462
- HTTP: 118 alive / 88 gold
- HTTPS: 116 alive / 34 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 190 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46725
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
