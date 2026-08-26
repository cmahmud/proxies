# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 420
- HTTP: 99 alive / 71 gold
- HTTPS: 74 alive / 19 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37953
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
