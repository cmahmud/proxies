# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 388
- HTTP: 129 alive / 64 gold
- HTTPS: 38 alive / 12 gold
- SOCKS4: 185 alive / 154 gold
- SOCKS5: 206 alive / 158 gold

## Historical pool

- Discovered: 175423
- Ever alive: 33131
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
