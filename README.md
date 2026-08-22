# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 408
- HTTP: 275 alive / 81 gold
- HTTPS: 208 alive / 25 gold
- SOCKS4: 212 alive / 153 gold
- SOCKS5: 250 alive / 149 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32373
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
