# SyndProxy private pool

## Current pool

- Alive now: 1280
- Gold now: 593
- HTTP: 483 alive / 181 gold
- HTTPS: 317 alive / 111 gold
- SOCKS4: 237 alive / 145 gold
- SOCKS5: 243 alive / 156 gold

## Historical pool

- Discovered: 125593
- Ever alive: 19555
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
