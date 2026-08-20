# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 430
- HTTP: 207 alive / 87 gold
- HTTPS: 184 alive / 20 gold
- SOCKS4: 221 alive / 157 gold
- SOCKS5: 261 alive / 166 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27588
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
