# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 407
- HTTP: 114 alive / 66 gold
- HTTPS: 82 alive / 12 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38119
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
