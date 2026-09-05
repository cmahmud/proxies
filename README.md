# SyndProxy validated proxy pool

## Current pool

- Alive now: 403
- Gold now: 317
- HTTP: 121 alive / 79 gold
- HTTPS: 32 alive / 21 gold
- SOCKS4: 81 alive / 71 gold
- SOCKS5: 169 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47824
- Ever gold: 1497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
