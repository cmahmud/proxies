# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 427
- HTTP: 86 alive / 69 gold
- HTTPS: 94 alive / 31 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47313
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
