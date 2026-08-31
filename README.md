# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 480
- HTTP: 139 alive / 100 gold
- HTTPS: 122 alive / 44 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45039
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
