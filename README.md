# SyndProxy validated proxy pool

## Current pool

- Alive now: 458
- Gold now: 363
- HTTP: 75 alive / 44 gold
- HTTPS: 42 alive / 9 gold
- SOCKS4: 163 alive / 154 gold
- SOCKS5: 178 alive / 156 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33018
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
