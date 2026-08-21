# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 365
- HTTP: 206 alive / 74 gold
- HTTPS: 172 alive / 25 gold
- SOCKS4: 190 alive / 130 gold
- SOCKS5: 232 alive / 136 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29660
- Ever gold: 1134

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
