# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 361
- HTTP: 96 alive / 36 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 180 alive / 158 gold

## Historical pool

- Discovered: 171600
- Ever alive: 32940
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
