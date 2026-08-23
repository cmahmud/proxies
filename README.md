# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 349
- HTTP: 112 alive / 41 gold
- HTTPS: 48 alive / 8 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 164 alive / 146 gold

## Historical pool

- Discovered: 171068
- Ever alive: 32860
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
