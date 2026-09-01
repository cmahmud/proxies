# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 465
- HTTP: 134 alive / 93 gold
- HTTPS: 125 alive / 38 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46915
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
