# SyndProxy private pool

## Current pool

- Alive now: 1377
- Gold now: 412
- HTTP: 550 alive / 99 gold
- HTTPS: 350 alive / 31 gold
- SOCKS4: 235 alive / 139 gold
- SOCKS5: 242 alive / 143 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31730
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
