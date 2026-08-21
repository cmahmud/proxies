# SyndProxy private pool

## Current pool

- Alive now: 771
- Gold now: 374
- HTTP: 215 alive / 74 gold
- HTTPS: 125 alive / 24 gold
- SOCKS4: 193 alive / 130 gold
- SOCKS5: 238 alive / 146 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29663
- Ever gold: 1134

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
