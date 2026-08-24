# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 388
- HTTP: 113 alive / 52 gold
- HTTPS: 48 alive / 15 gold
- SOCKS4: 183 alive / 156 gold
- SOCKS5: 197 alive / 165 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33405
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
