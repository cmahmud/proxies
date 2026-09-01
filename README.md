# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 471
- HTTP: 136 alive / 96 gold
- HTTPS: 106 alive / 37 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46888
- Ever gold: 1455

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
