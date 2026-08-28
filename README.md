# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 401
- HTTP: 85 alive / 57 gold
- HTTPS: 77 alive / 19 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42744
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
