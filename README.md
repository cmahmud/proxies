# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 457
- HTTP: 142 alive / 87 gold
- HTTPS: 134 alive / 32 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 187 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46661
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
