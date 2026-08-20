# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 394
- HTTP: 233 alive / 82 gold
- HTTPS: 169 alive / 22 gold
- SOCKS4: 201 alive / 137 gold
- SOCKS5: 210 alive / 153 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27168
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
