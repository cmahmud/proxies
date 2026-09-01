# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 463
- HTTP: 121 alive / 90 gold
- HTTPS: 135 alive / 35 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 221 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46514
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
