# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 462
- HTTP: 128 alive / 93 gold
- HTTPS: 120 alive / 30 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 186 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46674
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
