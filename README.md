# SyndProxy private pool

## Current pool

- Alive now: 1546
- Gold now: 565
- HTTP: 634 alive / 205 gold
- HTTPS: 491 alive / 94 gold
- SOCKS4: 179 alive / 104 gold
- SOCKS5: 242 alive / 162 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24753
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
