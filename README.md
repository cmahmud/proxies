# SyndProxy private pool

## Current pool

- Alive now: 1106
- Gold now: 437
- HTTP: 360 alive / 106 gold
- HTTPS: 269 alive / 31 gold
- SOCKS4: 207 alive / 142 gold
- SOCKS5: 270 alive / 158 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28655
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
