# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 442
- HTTP: 98 alive / 76 gold
- HTTPS: 114 alive / 27 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 187 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47531
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
