# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 384
- HTTP: 259 alive / 88 gold
- HTTPS: 143 alive / 21 gold
- SOCKS4: 179 alive / 117 gold
- SOCKS5: 246 alive / 158 gold

## Historical pool

- Discovered: 166329
- Ever alive: 32394
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
