# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 423
- HTTP: 293 alive / 98 gold
- HTTPS: 221 alive / 25 gold
- SOCKS4: 242 alive / 144 gold
- SOCKS5: 266 alive / 156 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28154
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
