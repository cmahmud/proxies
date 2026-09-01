# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 474
- HTTP: 141 alive / 97 gold
- HTTPS: 127 alive / 38 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46945
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
