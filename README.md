# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 419
- HTTP: 86 alive / 63 gold
- HTTPS: 77 alive / 27 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47129
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
