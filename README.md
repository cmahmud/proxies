# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 401
- HTTP: 73 alive / 53 gold
- HTTPS: 45 alive / 19 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47107
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
