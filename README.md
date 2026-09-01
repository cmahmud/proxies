# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 422
- HTTP: 87 alive / 65 gold
- HTTPS: 82 alive / 28 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47131
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
