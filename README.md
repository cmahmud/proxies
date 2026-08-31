# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 463
- HTTP: 133 alive / 94 gold
- HTTPS: 144 alive / 29 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 216 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45996
- Ever gold: 1439

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
