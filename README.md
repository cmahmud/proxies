# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 466
- HTTP: 136 alive / 95 gold
- HTTPS: 140 alive / 36 gold
- SOCKS4: 184 alive / 164 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46920
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
