# SyndProxy private pool

## Current pool

- Alive now: 1233
- Gold now: 464
- HTTP: 422 alive / 129 gold
- HTTPS: 330 alive / 73 gold
- SOCKS4: 226 alive / 117 gold
- SOCKS5: 255 alive / 145 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17265
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
