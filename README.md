# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 405
- HTTP: 113 alive / 63 gold
- HTTPS: 65 alive / 21 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38956
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
