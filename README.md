# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 380
- HTTP: 139 alive / 64 gold
- HTTPS: 160 alive / 20 gold
- SOCKS4: 163 alive / 146 gold
- SOCKS5: 180 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39699
- Ever gold: 1301

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
