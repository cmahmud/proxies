# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 374
- HTTP: 102 alive / 58 gold
- HTTPS: 48 alive / 12 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 178 alive / 154 gold

## Historical pool

- Discovered: 174133
- Ever alive: 33060
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
