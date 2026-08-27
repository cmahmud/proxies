# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 401
- HTTP: 94 alive / 57 gold
- HTTPS: 60 alive / 20 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41698
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
