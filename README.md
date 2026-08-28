# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 401
- HTTP: 97 alive / 68 gold
- HTTPS: 101 alive / 11 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43058
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
