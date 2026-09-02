# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 440
- HTTP: 114 alive / 78 gold
- HTTPS: 112 alive / 25 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47561
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
