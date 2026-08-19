# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 485
- HTTP: 363 alive / 137 gold
- HTTPS: 260 alive / 78 gold
- SOCKS4: 203 alive / 120 gold
- SOCKS5: 223 alive / 150 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17868
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
