# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 197
- HTTP: 193 alive / 41 gold
- HTTPS: 98 alive / 6 gold
- SOCKS4: 86 alive / 66 gold
- SOCKS5: 139 alive / 84 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32748
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
