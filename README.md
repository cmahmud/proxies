# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 458
- HTTP: 123 alive / 88 gold
- HTTPS: 118 alive / 33 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 184 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46722
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
