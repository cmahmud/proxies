# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 519
- HTTP: 367 alive / 161 gold
- HTTPS: 245 alive / 86 gold
- SOCKS4: 220 alive / 140 gold
- SOCKS5: 216 alive / 132 gold

## Historical pool

- Discovered: 119875
- Ever alive: 18514
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
