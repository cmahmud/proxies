# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 370
- HTTP: 88 alive / 46 gold
- HTTPS: 44 alive / 11 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 188 alive / 158 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32963
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
