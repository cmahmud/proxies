# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 396
- HTTP: 81 alive / 62 gold
- HTTPS: 35 alive / 16 gold
- SOCKS4: 178 alive / 155 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48147
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
