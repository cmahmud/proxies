# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 455
- HTTP: 117 alive / 91 gold
- HTTPS: 129 alive / 29 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 225 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46556
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
