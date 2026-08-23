# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 373
- HTTP: 80 alive / 43 gold
- HTTPS: 34 alive / 10 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 172852
- Ever alive: 32984
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
