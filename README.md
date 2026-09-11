# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 433
- HTTP: 92 alive / 74 gold
- HTTPS: 42 alive / 25 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49156
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
