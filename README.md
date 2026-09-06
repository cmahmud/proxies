# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 401
- HTTP: 111 alive / 72 gold
- HTTPS: 61 alive / 19 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 180 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48089
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
