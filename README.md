# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 453
- HTTP: 127 alive / 86 gold
- HTTPS: 130 alive / 32 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46616
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
