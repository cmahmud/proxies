# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 445
- HTTP: 87 alive / 72 gold
- HTTPS: 104 alive / 32 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47440
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
