# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 401
- HTTP: 103 alive / 67 gold
- HTTPS: 92 alive / 21 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 173 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43068
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
