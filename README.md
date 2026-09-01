# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 467
- HTTP: 138 alive / 95 gold
- HTTPS: 132 alive / 37 gold
- SOCKS4: 183 alive / 164 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46920
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
