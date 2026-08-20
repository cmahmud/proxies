# SyndProxy private pool

## Current pool

- Alive now: 1616
- Gold now: 562
- HTTP: 695 alive / 200 gold
- HTTPS: 499 alive / 96 gold
- SOCKS4: 184 alive / 104 gold
- SOCKS5: 238 alive / 162 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24754
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
