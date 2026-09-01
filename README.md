# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 466
- HTTP: 143 alive / 94 gold
- HTTPS: 127 alive / 38 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46919
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
