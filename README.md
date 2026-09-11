# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 369
- HTTP: 97 alive / 69 gold
- HTTPS: 50 alive / 23 gold
- SOCKS4: 136 alive / 108 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48720
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
