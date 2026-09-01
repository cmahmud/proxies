# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 454
- HTTP: 119 alive / 87 gold
- HTTPS: 123 alive / 32 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46622
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
