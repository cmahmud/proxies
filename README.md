# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 401
- HTTP: 77 alive / 60 gold
- HTTPS: 50 alive / 19 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42803
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
