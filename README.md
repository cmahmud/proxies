# SyndProxy private pool

## Current pool

- Alive now: 1136
- Gold now: 445
- HTTP: 384 alive / 112 gold
- HTTPS: 285 alive / 34 gold
- SOCKS4: 198 alive / 143 gold
- SOCKS5: 269 alive / 156 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28648
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
