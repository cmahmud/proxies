# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 380
- HTTP: 121 alive / 56 gold
- HTTPS: 43 alive / 9 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 182 alive / 159 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33458
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
