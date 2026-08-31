# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 457
- HTTP: 114 alive / 90 gold
- HTTPS: 115 alive / 35 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45665
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
