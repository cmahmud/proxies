# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 393
- HTTP: 86 alive / 64 gold
- HTTPS: 40 alive / 15 gold
- SOCKS4: 187 alive / 158 gold
- SOCKS5: 179 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48154
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
