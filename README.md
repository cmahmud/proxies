# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 417
- HTTP: 89 alive / 60 gold
- HTTPS: 69 alive / 21 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36145
- Ever gold: 1268

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
