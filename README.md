# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 374
- HTTP: 82 alive / 43 gold
- HTTPS: 37 alive / 12 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 198 alive / 161 gold

## Historical pool

- Discovered: 172322
- Ever alive: 32984
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
