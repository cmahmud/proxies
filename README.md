# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 465
- HTTP: 113 alive / 92 gold
- HTTPS: 96 alive / 37 gold
- SOCKS4: 189 alive / 163 gold
- SOCKS5: 235 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45692
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
