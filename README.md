# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 405
- HTTP: 110 alive / 61 gold
- HTTPS: 92 alive / 12 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 197 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38151
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
