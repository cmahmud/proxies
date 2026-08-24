# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 435
- HTTP: 127 alive / 79 gold
- HTTPS: 102 alive / 23 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34475
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
