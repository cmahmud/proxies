# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 401
- HTTP: 79 alive / 59 gold
- HTTPS: 55 alive / 20 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 174 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42825
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
