# SyndProxy validated proxy pool

## Current pool

- Alive now: 438
- Gold now: 360
- HTTP: 66 alive / 42 gold
- HTTPS: 31 alive / 11 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 176 alive / 154 gold

## Historical pool

- Discovered: 173735
- Ever alive: 33023
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
