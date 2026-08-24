# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 389
- HTTP: 93 alive / 62 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 161 alive / 156 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33437
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
