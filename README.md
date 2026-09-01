# SyndProxy validated proxy pool

## Current pool

- Alive now: 656
- Gold now: 462
- HTTP: 130 alive / 91 gold
- HTTPS: 125 alive / 34 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 224 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46525
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
