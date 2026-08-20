# SyndProxy private pool

## Current pool

- Alive now: 706
- Gold now: 352
- HTTP: 223 alive / 64 gold
- HTTPS: 126 alive / 20 gold
- SOCKS4: 181 alive / 132 gold
- SOCKS5: 176 alive / 136 gold

## Historical pool

- Discovered: 147175
- Ever alive: 25785
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
