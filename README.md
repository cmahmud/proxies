# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 450
- HTTP: 117 alive / 81 gold
- HTTPS: 88 alive / 34 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47000
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
