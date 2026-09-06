# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 393
- HTTP: 92 alive / 64 gold
- HTTPS: 47 alive / 16 gold
- SOCKS4: 178 alive / 155 gold
- SOCKS5: 182 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48153
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
