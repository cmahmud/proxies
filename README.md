# SyndProxy private pool

## Current pool

- Alive now: 874
- Gold now: 414
- HTTP: 248 alive / 94 gold
- HTTPS: 188 alive / 27 gold
- SOCKS4: 190 alive / 136 gold
- SOCKS5: 248 alive / 157 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29063
- Ever gold: 1122

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
