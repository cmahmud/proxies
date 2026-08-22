# SyndProxy private pool

## Current pool

- Alive now: 1067
- Gold now: 445
- HTTP: 335 alive / 95 gold
- HTTPS: 240 alive / 33 gold
- SOCKS4: 214 alive / 150 gold
- SOCKS5: 278 alive / 167 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31276
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
