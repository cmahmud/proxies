# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 398
- HTTP: 350 alive / 103 gold
- HTTPS: 250 alive / 32 gold
- SOCKS4: 204 alive / 122 gold
- SOCKS5: 258 alive / 141 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28043
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
