# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 468
- HTTP: 123 alive / 92 gold
- HTTPS: 140 alive / 36 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 228 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45912
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
