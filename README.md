# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 386
- HTTP: 115 alive / 53 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 198 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33388
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
