# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 403
- HTTP: 113 alive / 62 gold
- HTTPS: 59 alive / 20 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38956
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
