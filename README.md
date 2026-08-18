# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 320
- HTTP: 287 alive / 34 gold
- HTTPS: 196 alive / 10 gold
- SOCKS4: 234 alive / 144 gold
- SOCKS5: 242 alive / 132 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14210
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
