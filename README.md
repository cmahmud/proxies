# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 424
- HTTP: 303 alive / 93 gold
- HTTPS: 227 alive / 25 gold
- SOCKS4: 201 alive / 145 gold
- SOCKS5: 256 alive / 161 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28803
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
