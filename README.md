# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 389
- HTTP: 124 alive / 70 gold
- HTTPS: 56 alive / 14 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 177 alive / 152 gold

## Historical pool

- Discovered: 176956
- Ever alive: 33250
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
