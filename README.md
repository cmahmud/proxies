# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 423
- HTTP: 91 alive / 68 gold
- HTTPS: 100 alive / 28 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47283
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
