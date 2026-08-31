# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 466
- HTTP: 125 alive / 92 gold
- HTTPS: 136 alive / 34 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 228 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45918
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
