# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 456
- HTTP: 134 alive / 88 gold
- HTTPS: 149 alive / 31 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 186 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46633
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
