# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 429
- HTTP: 114 alive / 84 gold
- HTTPS: 146 alive / 19 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 195 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42264
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
