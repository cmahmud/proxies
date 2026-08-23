# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 219
- HTTP: 152 alive / 56 gold
- HTTPS: 134 alive / 11 gold
- SOCKS4: 92 alive / 68 gold
- SOCKS5: 152 alive / 84 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32683
- Ever gold: 1203

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
