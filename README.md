# SyndProxy private pool

## Current pool

- Alive now: 1607
- Gold now: 589
- HTTP: 663 alive / 198 gold
- HTTPS: 427 alive / 96 gold
- SOCKS4: 234 alive / 142 gold
- SOCKS5: 283 alive / 153 gold

## Historical pool

- Discovered: 136251
- Ever alive: 22754
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
