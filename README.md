# SyndProxy private pool

## Current pool

- Alive now: 949
- Gold now: 390
- HTTP: 311 alive / 84 gold
- HTTPS: 208 alive / 21 gold
- SOCKS4: 196 alive / 130 gold
- SOCKS5: 234 alive / 155 gold

## Historical pool

- Discovered: 144738
- Ever alive: 24989
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
