# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 414
- HTTP: 111 alive / 68 gold
- HTTPS: 78 alive / 20 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 173 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37757
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
