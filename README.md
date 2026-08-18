# SyndProxy private pool

## Current pool

- Alive now: 955
- Gold now: 249
- HTTP: 384 alive / 34 gold
- HTTPS: 193 alive / 6 gold
- SOCKS4: 223 alive / 145 gold
- SOCKS5: 155 alive / 64 gold

## Historical pool

- Discovered: 102867
- Ever alive: 13686
- Ever gold: 428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
