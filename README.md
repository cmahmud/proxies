# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 420
- HTTP: 81 alive / 65 gold
- HTTPS: 93 alive / 25 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47172
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
