# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 461
- HTTP: 150 alive / 91 gold
- HTTPS: 138 alive / 32 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 189 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46668
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
