# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 402
- HTTP: 346 alive / 101 gold
- HTTPS: 247 alive / 28 gold
- SOCKS4: 193 alive / 121 gold
- SOCKS5: 234 alive / 152 gold

## Historical pool

- Discovered: 152759
- Ever alive: 28350
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
