# SyndProxy private pool

## Current pool

- Alive now: 712
- Gold now: 376
- HTTP: 203 alive / 75 gold
- HTTPS: 97 alive / 16 gold
- SOCKS4: 219 alive / 142 gold
- SOCKS5: 193 alive / 143 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25440
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
