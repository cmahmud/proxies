# SyndProxy private pool

## Current pool

- Alive now: 1242
- Gold now: 387
- HTTP: 409 alive / 90 gold
- HTTPS: 293 alive / 19 gold
- SOCKS4: 242 alive / 137 gold
- SOCKS5: 298 alive / 141 gold

## Historical pool

- Discovered: 133962
- Ever alive: 21642
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
