# SyndProxy private pool

## Current pool

- Alive now: 1180
- Gold now: 400
- HTTP: 394 alive / 103 gold
- HTTPS: 276 alive / 25 gold
- SOCKS4: 205 alive / 129 gold
- SOCKS5: 305 alive / 143 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22601
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
