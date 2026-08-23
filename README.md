# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 358
- HTTP: 138 alive / 36 gold
- HTTPS: 53 alive / 9 gold
- SOCKS4: 190 alive / 156 gold
- SOCKS5: 209 alive / 157 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32930
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
