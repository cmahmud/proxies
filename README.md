# SyndProxy validated proxy pool

## Current pool

- Alive now: 689
- Gold now: 466
- HTTP: 146 alive / 97 gold
- HTTPS: 133 alive / 31 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 235 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46245
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
