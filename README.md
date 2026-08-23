# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 376
- HTTP: 96 alive / 52 gold
- HTTPS: 37 alive / 13 gold
- SOCKS4: 174 alive / 154 gold
- SOCKS5: 191 alive / 157 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33035
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
