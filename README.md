# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 516
- HTTP: 370 alive / 151 gold
- HTTPS: 254 alive / 87 gold
- SOCKS4: 210 alive / 145 gold
- SOCKS5: 205 alive / 133 gold

## Historical pool

- Discovered: 117170
- Ever alive: 17707
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
