# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 468
- HTTP: 142 alive / 94 gold
- HTTPS: 131 alive / 40 gold
- SOCKS4: 187 alive / 163 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46919
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
