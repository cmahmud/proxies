# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 375
- HTTP: 120 alive / 57 gold
- HTTPS: 47 alive / 8 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 190 alive / 154 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33325
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
