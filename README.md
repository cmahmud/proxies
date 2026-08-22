# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 409
- HTTP: 330 alive / 87 gold
- HTTPS: 255 alive / 24 gold
- SOCKS4: 220 alive / 150 gold
- SOCKS5: 250 alive / 148 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32287
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
