# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 459
- HTTP: 131 alive / 87 gold
- HTTPS: 120 alive / 33 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 196 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46729
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
