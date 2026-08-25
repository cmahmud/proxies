# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 421
- HTTP: 125 alive / 73 gold
- HTTPS: 94 alive / 21 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35285
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
