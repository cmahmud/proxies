# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 441
- HTTP: 96 alive / 72 gold
- HTTPS: 94 alive / 30 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 186 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47446
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
