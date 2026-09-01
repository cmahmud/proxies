# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 455
- HTTP: 135 alive / 85 gold
- HTTPS: 125 alive / 32 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46839
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
