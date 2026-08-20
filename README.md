# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 383
- HTTP: 236 alive / 77 gold
- HTTPS: 184 alive / 20 gold
- SOCKS4: 208 alive / 148 gold
- SOCKS5: 197 alive / 138 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26826
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
