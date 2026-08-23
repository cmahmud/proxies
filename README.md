# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 379
- HTTP: 81 alive / 47 gold
- HTTPS: 37 alive / 12 gold
- SOCKS4: 176 alive / 157 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 172315
- Ever alive: 32971
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
