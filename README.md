# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 418
- HTTP: 87 alive / 59 gold
- HTTPS: 41 alive / 24 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47094
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
