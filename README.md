# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 467
- HTTP: 133 alive / 90 gold
- HTTPS: 106 alive / 37 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 199 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46353
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
