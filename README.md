# SyndProxy validated proxy pool

## Current pool

- Alive now: 738
- Gold now: 462
- HTTP: 163 alive / 95 gold
- HTTPS: 148 alive / 30 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 244 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46275
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
