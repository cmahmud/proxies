# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 366
- HTTP: 91 alive / 42 gold
- HTTPS: 34 alive / 10 gold
- SOCKS4: 178 alive / 157 gold
- SOCKS5: 195 alive / 157 gold

## Historical pool

- Discovered: 173068
- Ever alive: 33009
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
