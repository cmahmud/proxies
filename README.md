# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 388
- HTTP: 121 alive / 53 gold
- HTTPS: 74 alive / 13 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 192 alive / 163 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33380
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
