# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 417
- HTTP: 122 alive / 68 gold
- HTTPS: 108 alive / 22 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35307
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
