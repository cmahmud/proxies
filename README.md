# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 401
- HTTP: 80 alive / 62 gold
- HTTPS: 51 alive / 16 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 176 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42831
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
