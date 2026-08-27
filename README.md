# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 418
- HTTP: 98 alive / 74 gold
- HTTPS: 115 alive / 20 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42002
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
