# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 368
- HTTP: 320 alive / 72 gold
- HTTPS: 209 alive / 18 gold
- SOCKS4: 208 alive / 118 gold
- SOCKS5: 237 alive / 160 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26114
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
