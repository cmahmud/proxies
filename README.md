# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 466
- HTTP: 138 alive / 93 gold
- HTTPS: 121 alive / 39 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46908
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
