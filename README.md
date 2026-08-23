# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 360
- HTTP: 121 alive / 36 gold
- HTTPS: 52 alive / 8 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 212 alive / 157 gold

## Historical pool

- Discovered: 171589
- Ever alive: 32930
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
