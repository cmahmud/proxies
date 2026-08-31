# SyndProxy validated proxy pool

## Current pool

- Alive now: 685
- Gold now: 464
- HTTP: 143 alive / 92 gold
- HTTPS: 130 alive / 34 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 234 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46213
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
