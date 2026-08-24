# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 410
- HTTP: 112 alive / 72 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33724
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
