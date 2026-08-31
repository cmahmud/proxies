# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 466
- HTTP: 115 alive / 92 gold
- HTTPS: 104 alive / 37 gold
- SOCKS4: 189 alive / 163 gold
- SOCKS5: 234 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45696
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
