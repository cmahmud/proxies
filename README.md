# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 416
- HTTP: 89 alive / 64 gold
- HTTPS: 43 alive / 20 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48858
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
