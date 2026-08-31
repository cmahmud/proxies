# SyndProxy validated proxy pool

## Current pool

- Alive now: 689
- Gold now: 455
- HTTP: 143 alive / 90 gold
- HTTPS: 148 alive / 30 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 225 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46069
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
