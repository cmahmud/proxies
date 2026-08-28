# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 440
- HTTP: 127 alive / 85 gold
- HTTPS: 139 alive / 22 gold
- SOCKS4: 188 alive / 163 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42224
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
