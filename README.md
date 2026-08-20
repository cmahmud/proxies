# SyndProxy private pool

## Current pool

- Alive now: 775
- Gold now: 372
- HTTP: 247 alive / 72 gold
- HTTPS: 113 alive / 15 gold
- SOCKS4: 232 alive / 149 gold
- SOCKS5: 183 alive / 136 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25450
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
