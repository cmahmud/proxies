# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 473
- HTTP: 151 alive / 93 gold
- HTTPS: 131 alive / 42 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 195 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46938
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
