# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 516
- HTTP: 369 alive / 150 gold
- HTTPS: 262 alive / 88 gold
- SOCKS4: 207 alive / 146 gold
- SOCKS5: 205 alive / 132 gold

## Historical pool

- Discovered: 117170
- Ever alive: 17707
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
