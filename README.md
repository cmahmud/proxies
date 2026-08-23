# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 375
- HTTP: 87 alive / 46 gold
- HTTPS: 47 alive / 12 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 192 alive / 161 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32963
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
