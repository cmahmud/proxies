# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 409
- HTTP: 91 alive / 63 gold
- HTTPS: 95 alive / 21 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 176 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47202
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
