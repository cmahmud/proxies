# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 458
- HTTP: 141 alive / 87 gold
- HTTPS: 128 alive / 35 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46861
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
