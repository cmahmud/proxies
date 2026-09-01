# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 462
- HTTP: 143 alive / 90 gold
- HTTPS: 128 alive / 36 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46865
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
