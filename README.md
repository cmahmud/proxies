# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 465
- HTTP: 129 alive / 92 gold
- HTTPS: 126 alive / 36 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 223 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46494
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
