# SyndProxy validated proxy pool

## Current pool

- Alive now: 448
- Gold now: 368
- HTTP: 69 alive / 47 gold
- HTTPS: 36 alive / 8 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 178 alive / 157 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33020
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
