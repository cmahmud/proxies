# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 455
- HTTP: 120 alive / 88 gold
- HTTPS: 125 alive / 32 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 225 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46546
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
