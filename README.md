# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 444
- HTTP: 337 alive / 105 gold
- HTTPS: 233 alive / 31 gold
- SOCKS4: 192 alive / 148 gold
- SOCKS5: 272 alive / 160 gold

## Historical pool

- Discovered: 153732
- Ever alive: 28677
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
