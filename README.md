# SyndProxy private pool

## Current pool

- Alive now: 1107
- Gold now: 417
- HTTP: 339 alive / 94 gold
- HTTPS: 265 alive / 27 gold
- SOCKS4: 243 alive / 150 gold
- SOCKS5: 260 alive / 146 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25196
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
