# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 466
- HTTP: 132 alive / 90 gold
- HTTPS: 122 alive / 37 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 221 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46489
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
