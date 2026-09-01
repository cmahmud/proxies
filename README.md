# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 467
- HTTP: 141 alive / 94 gold
- HTTPS: 133 alive / 36 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 200 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46932
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
