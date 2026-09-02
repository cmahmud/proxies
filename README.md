# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 438
- HTTP: 93 alive / 73 gold
- HTTPS: 90 alive / 29 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47444
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
