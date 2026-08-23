# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 360
- HTTP: 121 alive / 36 gold
- HTTPS: 50 alive / 8 gold
- SOCKS4: 195 alive / 159 gold
- SOCKS5: 208 alive / 157 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32930
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
