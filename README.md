# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 435
- HTTP: 342 alive / 113 gold
- HTTPS: 196 alive / 32 gold
- SOCKS4: 251 alive / 149 gold
- SOCKS5: 258 alive / 141 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30780
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
