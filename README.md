# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 462
- HTTP: 135 alive / 92 gold
- HTTPS: 133 alive / 35 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46683
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
