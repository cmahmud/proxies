# SyndProxy private pool

## Current pool

- Alive now: 1153
- Gold now: 378
- HTTP: 377 alive / 94 gold
- HTTPS: 244 alive / 15 gold
- SOCKS4: 230 alive / 136 gold
- SOCKS5: 302 alive / 133 gold

## Historical pool

- Discovered: 131826
- Ever alive: 20990
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
