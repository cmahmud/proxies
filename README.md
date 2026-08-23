# SyndProxy validated proxy pool

## Current pool

- Alive now: 366
- Gold now: 216
- HTTP: 135 alive / 53 gold
- HTTPS: 41 alive / 10 gold
- SOCKS4: 72 alive / 69 gold
- SOCKS5: 118 alive / 84 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32692
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
