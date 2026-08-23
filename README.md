# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 368
- HTTP: 80 alive / 44 gold
- HTTPS: 39 alive / 10 gold
- SOCKS4: 177 alive / 155 gold
- SOCKS5: 184 alive / 159 gold

## Historical pool

- Discovered: 173048
- Ever alive: 32990
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
