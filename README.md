# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 454
- HTTP: 117 alive / 87 gold
- HTTPS: 113 alive / 31 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45658
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
