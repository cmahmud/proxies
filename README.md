# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 445
- HTTP: 356 alive / 104 gold
- HTTPS: 244 alive / 31 gold
- SOCKS4: 208 alive / 147 gold
- SOCKS5: 269 alive / 163 gold

## Historical pool

- Discovered: 153731
- Ever alive: 28661
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
