# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 388
- HTTP: 117 alive / 64 gold
- HTTPS: 45 alive / 16 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 182 alive / 154 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33258
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
