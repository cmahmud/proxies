# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 389
- HTTP: 314 alive / 90 gold
- HTTPS: 220 alive / 33 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 230 alive / 130 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31284
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
