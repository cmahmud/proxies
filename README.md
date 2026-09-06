# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 394
- HTTP: 122 alive / 81 gold
- HTTPS: 57 alive / 22 gold
- SOCKS4: 159 alive / 138 gold
- SOCKS5: 186 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48034
- Ever gold: 1514

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
