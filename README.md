# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 433
- HTTP: 116 alive / 81 gold
- HTTPS: 92 alive / 23 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34019
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
