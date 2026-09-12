# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 421
- HTTP: 116 alive / 76 gold
- HTTPS: 44 alive / 22 gold
- SOCKS4: 182 alive / 159 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49474
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
