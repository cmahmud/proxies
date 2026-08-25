# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 406
- HTTP: 114 alive / 63 gold
- HTTPS: 91 alive / 20 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35446
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
