# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 378
- HTTP: 86 alive / 46 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 190 alive / 162 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33558
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
