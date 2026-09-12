# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 413
- HTTP: 94 alive / 73 gold
- HTTPS: 44 alive / 18 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49463
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
