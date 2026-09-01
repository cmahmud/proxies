# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 454
- HTTP: 132 alive / 90 gold
- HTTPS: 145 alive / 29 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 216 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46584
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
