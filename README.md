# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 474
- HTTP: 145 alive / 94 gold
- HTTPS: 122 alive / 42 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46938
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
