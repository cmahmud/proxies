# SyndProxy validated proxy pool

## Current pool

- Alive now: 695
- Gold now: 462
- HTTP: 151 alive / 95 gold
- HTTPS: 126 alive / 29 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 243 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46262
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
