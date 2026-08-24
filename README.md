# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 411
- HTTP: 148 alive / 68 gold
- HTTPS: 72 alive / 18 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33704
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
