# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 399
- HTTP: 164 alive / 68 gold
- HTTPS: 51 alive / 15 gold
- SOCKS4: 172 alive / 156 gold
- SOCKS5: 189 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33283
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
