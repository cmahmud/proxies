# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 428
- HTTP: 126 alive / 78 gold
- HTTPS: 74 alive / 23 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33937
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
