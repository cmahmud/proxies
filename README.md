# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 401
- HTTP: 105 alive / 75 gold
- HTTPS: 39 alive / 18 gold
- SOCKS4: 168 alive / 152 gold
- SOCKS5: 183 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48235
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
