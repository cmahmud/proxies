# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 376
- HTTP: 94 alive / 61 gold
- HTTPS: 41 alive / 10 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 175 alive / 154 gold

## Historical pool

- Discovered: 174307
- Ever alive: 33080
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
