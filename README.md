# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 356
- HTTP: 96 alive / 36 gold
- HTTPS: 50 alive / 10 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 179 alive / 156 gold

## Historical pool

- Discovered: 171600
- Ever alive: 32940
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
