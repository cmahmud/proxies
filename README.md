# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 476
- HTTP: 138 alive / 97 gold
- HTTPS: 122 alive / 39 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46951
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
