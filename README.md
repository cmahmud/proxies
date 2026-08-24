# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 399
- HTTP: 164 alive / 68 gold
- HTTPS: 44 alive / 15 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 191 alive / 159 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33283
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
