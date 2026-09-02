# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 441
- HTTP: 122 alive / 76 gold
- HTTPS: 108 alive / 28 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47566
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
