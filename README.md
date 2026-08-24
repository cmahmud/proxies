# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 388
- HTTP: 107 alive / 55 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33389
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
