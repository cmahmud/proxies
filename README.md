# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 460
- HTTP: 121 alive / 88 gold
- HTTPS: 122 alive / 31 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 195 alive / 181 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46776
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
