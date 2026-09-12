# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 365
- HTTP: 91 alive / 64 gold
- HTTPS: 44 alive / 16 gold
- SOCKS4: 156 alive / 136 gold
- SOCKS5: 162 alive / 149 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49559
- Ever gold: 1587

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
