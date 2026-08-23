# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 351
- HTTP: 120 alive / 33 gold
- HTTPS: 36 alive / 7 gold
- SOCKS4: 164 alive / 154 gold
- SOCKS5: 175 alive / 157 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32950
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
