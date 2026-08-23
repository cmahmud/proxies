# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 375
- HTTP: 100 alive / 58 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 165 alive / 151 gold
- SOCKS5: 176 alive / 154 gold

## Historical pool

- Discovered: 174129
- Ever alive: 33060
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
