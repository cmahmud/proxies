# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 363
- HTTP: 69 alive / 40 gold
- HTTPS: 34 alive / 9 gold
- SOCKS4: 177 alive / 157 gold
- SOCKS5: 184 alive / 157 gold

## Historical pool

- Discovered: 173068
- Ever alive: 33009
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
