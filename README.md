# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 389
- HTTP: 91 alive / 63 gold
- HTTPS: 86 alive / 17 gold
- SOCKS4: 159 alive / 154 gold
- SOCKS5: 174 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43328
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
