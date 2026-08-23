# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 363
- HTTP: 108 alive / 38 gold
- HTTPS: 49 alive / 10 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 196 alive / 158 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32935
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
