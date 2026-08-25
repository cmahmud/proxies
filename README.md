# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 424
- HTTP: 131 alive / 73 gold
- HTTPS: 89 alive / 23 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35127
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
