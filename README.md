# SyndProxy private pool

## Current pool

- Alive now: 1366
- Gold now: 464
- HTTP: 507 alive / 112 gold
- HTTPS: 351 alive / 31 gold
- SOCKS4: 242 alive / 160 gold
- SOCKS5: 266 alive / 161 gold

## Historical pool

- Discovered: 160011
- Ever alive: 30508
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
