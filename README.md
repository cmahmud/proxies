# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 391
- HTTP: 80 alive / 56 gold
- HTTPS: 96 alive / 13 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 175 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42933
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
