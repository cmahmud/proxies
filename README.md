# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 416
- HTTP: 82 alive / 65 gold
- HTTPS: 50 alive / 22 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 177 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47076
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
