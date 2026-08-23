# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 376
- HTTP: 94 alive / 63 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 161 alive / 150 gold
- SOCKS5: 174 alive / 153 gold

## Historical pool

- Discovered: 174307
- Ever alive: 33080
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
