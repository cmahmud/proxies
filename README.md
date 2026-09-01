# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 468
- HTTP: 149 alive / 95 gold
- HTTPS: 129 alive / 34 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 193 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46328
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
