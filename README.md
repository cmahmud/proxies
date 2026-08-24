# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 436
- HTTP: 126 alive / 81 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34003
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
