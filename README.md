# SyndProxy validated proxy pool

## Current pool

- Alive now: 412
- Gold now: 348
- HTTP: 102 alive / 70 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 91 alive / 88 gold
- SOCKS5: 174 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48689
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
