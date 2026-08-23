# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 357
- HTTP: 129 alive / 35 gold
- HTTPS: 54 alive / 8 gold
- SOCKS4: 191 alive / 157 gold
- SOCKS5: 211 alive / 157 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32930
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
