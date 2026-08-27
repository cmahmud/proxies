# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 422
- HTTP: 95 alive / 76 gold
- HTTPS: 75 alive / 23 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 176 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41765
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
