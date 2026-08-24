# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 380
- HTTP: 92 alive / 52 gold
- HTTPS: 36 alive / 13 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 196 alive / 160 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33346
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
