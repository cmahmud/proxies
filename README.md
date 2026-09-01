# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 421
- HTTP: 86 alive / 68 gold
- HTTPS: 93 alive / 27 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47261
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
