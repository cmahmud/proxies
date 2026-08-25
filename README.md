# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 418
- HTTP: 94 alive / 64 gold
- HTTPS: 74 alive / 20 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 185 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35614
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
