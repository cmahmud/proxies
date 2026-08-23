# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 368
- HTTP: 76 alive / 41 gold
- HTTPS: 35 alive / 12 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 172855
- Ever alive: 32985
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
