# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 388
- HTTP: 95 alive / 66 gold
- HTTPS: 45 alive / 18 gold
- SOCKS4: 167 alive / 129 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48748
- Ever gold: 1565

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
