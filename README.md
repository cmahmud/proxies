# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 376
- HTTP: 92 alive / 48 gold
- HTTPS: 40 alive / 13 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 195 alive / 160 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32958
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
