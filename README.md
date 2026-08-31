# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 457
- HTTP: 113 alive / 90 gold
- HTTPS: 114 alive / 35 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45665
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
