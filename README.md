# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 473
- HTTP: 150 alive / 93 gold
- HTTPS: 127 alive / 42 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 196 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46939
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
