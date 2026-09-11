# SyndProxy validated proxy pool

## Current pool

- Alive now: 444
- Gold now: 356
- HTTP: 113 alive / 72 gold
- HTTPS: 54 alive / 20 gold
- SOCKS4: 99 alive / 94 gold
- SOCKS5: 178 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48700
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
