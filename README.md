# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 196
- HTTP: 158 alive / 42 gold
- HTTPS: 41 alive / 8 gold
- SOCKS4: 138 alive / 64 gold
- SOCKS5: 158 alive / 82 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32724
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
