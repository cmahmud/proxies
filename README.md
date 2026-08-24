# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 385
- HTTP: 93 alive / 52 gold
- HTTPS: 29 alive / 12 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33391
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
