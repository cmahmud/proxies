# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 403
- HTTP: 107 alive / 62 gold
- HTTPS: 55 alive / 19 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38956
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
