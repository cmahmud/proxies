# SyndProxy private pool

## Current pool

- Alive now: 1856
- Gold now: 617
- HTTP: 819 alive / 233 gold
- HTTPS: 607 alive / 118 gold
- SOCKS4: 181 alive / 104 gold
- SOCKS5: 249 alive / 162 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24768
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
