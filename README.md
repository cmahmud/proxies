# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 463
- HTTP: 133 alive / 94 gold
- HTTPS: 123 alive / 32 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 185 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46674
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
