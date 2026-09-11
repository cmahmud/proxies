# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 445
- HTTP: 111 alive / 82 gold
- HTTPS: 46 alive / 29 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 180 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49210
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
