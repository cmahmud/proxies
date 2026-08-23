# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 219
- HTTP: 153 alive / 56 gold
- HTTPS: 133 alive / 11 gold
- SOCKS4: 96 alive / 68 gold
- SOCKS5: 154 alive / 84 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32683
- Ever gold: 1203

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
