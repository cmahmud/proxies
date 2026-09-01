# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 474
- HTTP: 149 alive / 96 gold
- HTTPS: 131 alive / 40 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46940
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
