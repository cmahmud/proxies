# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 401
- HTTP: 103 alive / 76 gold
- HTTPS: 42 alive / 16 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 170 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48191
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
