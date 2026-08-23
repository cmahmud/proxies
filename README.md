# SyndProxy validated proxy pool

## Current pool

- Alive now: 434
- Gold now: 363
- HTTP: 64 alive / 41 gold
- HTTPS: 31 alive / 11 gold
- SOCKS4: 162 alive / 156 gold
- SOCKS5: 177 alive / 155 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33020
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
