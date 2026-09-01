# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 450
- HTTP: 121 alive / 82 gold
- HTTPS: 131 alive / 32 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46746
- Ever gold: 1448

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
