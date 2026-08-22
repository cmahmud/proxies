# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 434
- HTTP: 351 alive / 99 gold
- HTTPS: 260 alive / 33 gold
- SOCKS4: 190 alive / 131 gold
- SOCKS5: 258 alive / 171 gold

## Historical pool

- Discovered: 161922
- Ever alive: 31170
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
