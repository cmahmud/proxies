# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 404
- HTTP: 76 alive / 49 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47103
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
